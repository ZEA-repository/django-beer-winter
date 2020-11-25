from bars.models import Bar, Address
from django.db import IntegrityError
from django.http import JsonResponse
import json
import time
import requests

from bars.services.parseData import Parse
from bars.services.randomDescriptionToDB import random_description_db


def lambic_to_db():
	""" latitude and longitude save to db """

	if len(Bar.objects.filter(title="lambic")) == 0:
		Bar.objects.create(title="lambic")

	titleId = Bar.objects.filter(title="lambic").values("id")[0]["id"]
	barItem = Bar.objects.get(id=titleId)
	
	lambic_obj = Parse(
		url="https://lambicbar.ru/address", selector=".restaurant > .h3"
	)

	addresses = lambic_obj.lambic()
	url = "https://us1.locationiq.com/v1/search.php" 
	for address in addresses:
		time.sleep(5)
		data = {"key": "pk.f20a2a3850152096ecbf64880a9acaeb", "q": address, "format": "json"}
		response = requests.get(url, params=data)
		data = json.loads(response.text)[0]
		try:
			barItem.address_set.create(lat=data["lat"], lon=data["lon"], description=random_description_db(1))
		except IntegrityError:
			print("record didn't write because alredy exist")
	return "successful"

def mannekenPis_to_db():
	""" latitude and longitude save to db """

	if len(Bar.objects.filter(title="manneken pis")) == 0:
		Bar.objects.create(title="manneken pis")

	titleId = Bar.objects.filter(title="manneken pis").values("id")[0]["id"]
	barItem = Bar.objects.get(id=titleId)

	mannekenPis_obj = Parse(
		url="http://reca.rest/restaurants", selector=".item-description-place"
	)

	address = mannekenPis_obj.manneken_pis()   
	url = "https://us1.locationiq.com/v1/search.php"
	time.sleep(5)
	data = {"key": "pk.f20a2a3850152096ecbf64880a9acaeb", "q": address, "format": "json"}
	response = requests.get(url, params=data)
	data = json.loads(response.text)[0]
	try:
		barItem.address_set.create(lat=data["lat"], lon=data["lon"], description=random_description_db(1))
	except IntegrityError:
		print("record didn't write because alredy exist")

	return "successful"