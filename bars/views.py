# /usr/local/lib/python3.6/dist-packages

from django.shortcuts import render

from bars.services import (
		parseData,
		randomDescriptionToDB,
		convertAddressesToGPS
	)


def index(request):
	context = {
		

	}
	return render(request, "index.html", context)

def show_address_on_map(request):
	return render(request, "map.html", {})
