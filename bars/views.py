# /usr/local/lib/python3.6/dist-packages

from django.shortcuts import render

from bars.services import (
		parseData,
		randomDescriptionToDB,
		convertAddressesToGPS
	)


def index(request):
	return render(request, "index.html", {})

def show_address_on_map(request):
	return render(request, "map.html", {})
