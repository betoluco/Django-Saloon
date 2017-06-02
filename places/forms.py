from django.contrib.gis import forms
from django.forms import Textarea, modelformset_factory

from places.models import Place


class LatLngWidget(forms.MultiWidget):
	'''
	A widget that splits Point in two longitude/latitude text inputs
	'''
	def __init__(self):
		widgets = (
			forms.TextInput(attrs={'placeholder':'Latitude'}),
			forms.TextInput(attrs={'placeholder':'Longitude'})
		)

		super(LatLngWidget, self).__init__(widgets)

	def decompress(self, value):
		if value:
			return tuple(reversed(value.coords))
		return (None, None)

class LatLngField(forms.MultiValueField):

	widget = LatLngWidget

	def __init__(self):

		fields=(forms.FloatField(min_value=-90, max_value=90), forms.FloatField(min_value=-180, max_value=180))
		super(LatLngField, self).__init__(fields=fields)

	def compress(self, data_list):
		return 'POINT(%f %f)'%tuple(reversed(data_list))


class PlacesForm(forms.ModelForm):

	latitude_longitude = LatLngField()

	class Meta:
		model = Place
		fields = '__all__'
		widgets = {'description': Textarea(),}