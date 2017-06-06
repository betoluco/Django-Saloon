from django.shortcuts import render
from django.contrib.gis.geos import Polygon
from django.core.paginator import Paginator, PageNotAnInteger

from places.models import Place


def home_page(request):
	places = Place.objects.filter(active=True)
	return render(request, 'places/home_page.html', {'places': places})

def results(request):
	corners = (request.GET['swLng'], request.GET['swLat'], request.GET['neLng'], request.GET['neLat'])
	geom = Polygon.from_bbox(corners)
	paginator =	Paginator(Place.objects.filter(active=True).filter(latitude_longitude__within=geom), 5)
	page = request.GET.get('page')
	try:
		results = paginator.page(page)
	except PageNotAnInteger:
		results = paginator.page(1)
	return render(request, 'places/results.html', {'results': results})