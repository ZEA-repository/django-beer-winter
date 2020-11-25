import json


def get_title_description_coordinates(sum_bars):
	with open("./static/fmapbox.geojson", "w") as write_file, open("fixture.json", "r") as fixture:
		data = json.load(fixture)
		objects = []
		properties = []
		geometryCoordinates = []
		for line in data:
			for bar_id in range(1, sum_bars+1):
				if line["model"] == "bars.bar" and line["pk"] == bar_id:
					properties.append({
						"id": bar_id,
						"title": line["fields"]["title"]
						})
				elif line["model"] == "bars.address" and line["fields"]["bar"] == bar_id:
					geometryCoordinates.append({
						"id": bar_id,
						"lon": line["fields"]["lon"],
						"lat": line["fields"]["lat"],
						"description": line["fields"]["description"]
						})
		fmapbox = {}
		places = []
		for bar_id in range(1, sum_bars+1):
			for objCoordinate in geometryCoordinates:
				for objProp in properties:
					if objCoordinate["id"] == bar_id and objProp["id"] == bar_id:
						lon = objCoordinate["lon"]
						lat = objCoordinate["lat"] 
						title = objProp["title"]
						description = objCoordinate["description"]
						places.append({
							"type": "Feature",
							"properties": {
								"title": title,
								"description": description,
								"icon": "beer"
							},
							"geometry": {
								"coordinates": [lon, lat],
								"type": "Point"
							}
							})

						fmapbox["features"] = places
						fmapbox["type"] = "FeatureCollection"
		json.dump(fmapbox, write_file, indent=2)
	return f"create/update fmapbox.geojson is done"

print(get_title_description_coordinates(2))	
