import json
from django.shortcuts import render
from django.contrib.gis.geos import Polygon
from django.core.paginator import Paginator, PageNotAnInteger

from places.models import Place

PER_PAGE = 10

def home_page(request):
	return render(request, 'places/home_page.html')

def results(request):
	box = json.loads(request.GET['bounds'])
	poly = Polygon.from_bbox((box['west'], box['south'], box['east'], box['north']))
	markers = Place.objects.filter(active=True).filter(latitude_longitude__within=poly)
	results = Paginator(markers, PER_PAGE)
	page = results.page(request.GET.get('page', 1))
	return render(request, 'places/results.html', {'results': page, 'markers': markers})

def place(request):
	place = Place.objects.get(pk=request.GET['place'])
	return render(request, 'places/place.html', {'place': place})
