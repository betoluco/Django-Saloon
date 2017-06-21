import json
from django.shortcuts import render
from django.contrib.gis.geos import Polygon
from django.core.paginator import Paginator, PageNotAnInteger

from places.models import Place


def home_page(request):
	return render(request, 'places/home_page.html', {'places':Place.objects.filter(active=True)})

def results(request):
	box = json.loads(request.GET['bounds'])
	poly = Polygon.from_bbox((box['west'], box['south'], box['east'], box['north']))
	paginator =	Paginator(Place.objects.filter(active=True).filter(latitude_longitude__within=poly), 5)
	page = request.GET.get('page')
	try:
		results = paginator.page(page)
	except PageNotAnInteger:
		results = paginator.page(1)
	return render(request, 'places/results.html', {'results': results})

def place(request):
	place = Place.objects.get(pk=request.GET['place'])
	return render(request, 'places/place.html', {'place': place})