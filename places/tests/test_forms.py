from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.gis.geos import GEOSGeometry
from django.forms.widgets import Textarea, TextInput

from places.forms import PlacesForm, LatLngField, LatLngWidget
from places.models import Place

FILE_PATH = 'places/tests/test_img.png'

class PlaceModelFormTest(TestCase):

	def form_creator(self):
		data = {
			"name": "Place name",
			"description": "Place type",
			"indoors_capacity": 100,
			"outdoors_capacity": 100,
			"min_capacity": 100,
			"parking_capacity": 10,
			"kitchen_sqrt_m": 10,
			"restrooms": True,
			"ac": True,
			"heating": True,
			"aux_power_generator": True,
			"games": True,
			"active": True,
			"last_modified": "2016-01-29",
			"latitude_longitude_0": 10.0,
			"latitude_longitude_1": 10.0
		}
		place_form =  PlacesForm(data)
		return place_form


	def test_form_validates_the_data(self):
		place_form = self.form_creator()
		self.assertTrue(place_form.is_valid())

	def test_description_is_rendered_as_a_textarea(self):
		place_form =  PlacesForm()
		self.assertIsInstance(place_form.fields['description'].widget, Textarea)

	def test_indoors_capacity_can_be_left_blank(self):
		place_form = self.form_creator()
		place_form.data['indoors_capacity'] =  ''
		self.assertTrue(place_form.is_valid())

	def test_outdoors_capacity_can_be_left_blank(self):
		place_form = self.form_creator()
		place_form.data['outdoors_capacity'] = ''
		self.assertTrue(place_form.is_valid())

	def test_min_capacity_can_be_left_blank(self):
		place_form = self.form_creator()
		place_form.data['min_capacity'] = ''
		self.assertTrue(place_form.is_valid())

	def test_parking_capacity_can_be_left_blank(self):
		place_form = self.form_creator()
		place_form.data['parking_capacity'] = ''
		self.assertTrue(place_form.is_valid())

	def test_kitchen_sqrt_m_can_be_left_blank(self):
		place_form = self.form_creator()
		place_form.data['kitchen_sqrt_m'] = ''
		self.assertTrue(place_form.is_valid())

	def test_latitude_longitude_0_field_accepts_values_lesser_or_equal_than_90(self):
		place_form = self.form_creator()
		place_form.data['latitude_longitude_0'] = 90
		self.assertTrue(place_form.is_valid())
		place_form_1 = self.form_creator()
		place_form_1.data['latitude_longitude_0'] = 90.000001
		self.assertFalse(place_form_1.is_valid())

	def test_latitude_longitude_0_field_accepts_values_greater_or_equal_than_minus_90(self):
		place_form = self.form_creator()
		place_form.data['latitude_longitude_0'] = -90
		self.assertTrue(place_form.is_valid())
		place_form_1 = self.form_creator()
		place_form_1.data['latitude_longitude_0'] = -90.000001
		self.assertFalse(place_form_1.is_valid())

	def test_latitude_longitude_0_field_accepts_values_lesser_or_equal_than_180(self):
		place_form = self.form_creator()
		place_form.data['latitude_longitude_1'] = 180
		self.assertTrue(place_form.is_valid())
		place_form_1 = self.form_creator()
		place_form_1.data['latitude_longitude_0'] = 180.000001
		self.assertFalse(place_form_1.is_valid())

	def test_latitude_longitude_0_field_accepts_values_greater_or_equal_than_minus_180(self):
		place_form = self.form_creator()
		place_form.data['latitude_longitude_1'] = -180
		self.assertTrue(place_form.is_valid())
		place_form_1 = self.form_creator()
		place_form_1.data['latitude_longitude_0'] = -180.000001
		self.assertFalse(place_form_1.is_valid())

	def test_LatLngField_is_made_of_two_text_inputs(self):
		self.assertIsInstance(LatLngField().widget.widgets[0], TextInput)
		self.assertIsInstance(LatLngField().widget.widgets[1], TextInput)
	
	def test_LatLngField_has_latitude_longitude_placeholders(self):
		self.assertIn(
			'placeholder="Latitude"',
			LatLngField().widget.render('test', [None, None])
		)
		self.assertIn(
			'placeholder="Longitude"',
			LatLngField().widget.render('test', [None, None])
		)

	def test_LatLngWidget_correctly_decompress_the_values(self):
		point = GEOSGeometry('POINT (10 10)')
		lat_lng_widget = LatLngWidget()
		self.assertEqual((10, 10), lat_lng_widget.decompress(point))

	def test_LatLngWidget_correctly_handles_null_values_when_decompressing(self):
		lat_lng_widget = LatLngWidget()
		self.assertEqual((None, None), lat_lng_widget.decompress(None))
