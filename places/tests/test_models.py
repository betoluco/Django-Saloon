import os
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.core.files.images import ImageFile
from django.forms import ModelForm
from django.forms.widgets import Select
from datetime import date

from places.models import Place, Region, Locality, Address, Telephone, Email, Representative, SocialMedia, ProfilePicture, Picture
from website.settings.local import MEDIA_URL


PICTURES_PATH = 'places/tests/pictures/'


class PlaceTest(TestCase):
	
	def place_cretator(self):
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
			"latitude_longitude": "POINT(-99.738952 19.296423)",
		}
		place = Place(**data)
		return place

	def test_place_model_fields_can_store_in_the_database_the_correct_data(self):
		place = self.place_cretator()
		place.save()
		self.assertEqual(Place.objects.count(), 1)

	def test_some_place_model_fields_can_accept_null_and_blank_values(self):
		place = Place(
			name='Place name',
			description='Place type',
			indoors_capacity=None,
			outdoors_capacity=None,
			min_capacity=None,
			parking_capacity=None,
			kitchen_sqrt_m=None,
			restrooms=False,
			ac=False,
			heating=False,
			aux_power_generator=False,
			games=False,
			active=True,
			last_modified='2016-01-29',
			latitude_longitude='POINT(19.284793 -99.507620)',
		)
		place.save()
		self.assertEqual(Place.objects.count(), 1)
	
	def test_indoors_capacity_trows_error_when_cero_is_given(self):
		place = self.place_cretator()
		place.indoors_capacity = 0 
		self.assertRaises(ValidationError, place.clean_fields)
		try:
			place.clean_fields()
		except ValidationError as ve:
			self.assertIn('indoors_capacity', ve.error_dict)

	def test_indoors_capacity_trows_error_when_negative_number_is_given(self):
		place = self.place_cretator()
		place.indoors_capacity = -1
		self.assertRaises(ValidationError, place.clean_fields)
		try:
			place.clean_fields()
		except ValidationError as ve:
			self.assertIn('indoors_capacity', ve.error_dict)

	def test_outdoors_capacity_trows_error_when_cero_is_given(self):
		place = self.place_cretator()
		place.outdoors_capacity = 0
		self.assertRaises(ValidationError, place.clean_fields)
		try:
			place.clean_fields()
		except ValidationError as ve:
			self.assertIn('outdoors_capacity', ve.error_dict)

	def test_outdoors_capacity_trows_error_when_negative_number_is_given(self):
		place = self.place_cretator()
		place.outdoors_capacity = -1
		self.assertRaises(ValidationError, place.clean_fields)
		try:
			place.clean_fields()
		except ValidationError as ve:
			self.assertIn('outdoors_capacity', ve.error_dict)

	def test_min_capacity_trows_error_when_cero_is_given(self):
		place = self.place_cretator()
		place.min_capacity = 0 
		self.assertRaises(ValidationError, place.clean_fields)
		try:
			place.clean_fields()
		except ValidationError as ve:
			self.assertIn('min_capacity', ve.error_dict)

	def test_min_capacity_trows_error_when_negative_number_is_given(self):
		place = self.place_cretator()
		place.min_capacity = -1
		self.assertRaises(ValidationError, place.clean_fields)
		try:
			place.clean_fields()
		except ValidationError as ve:
			self.assertIn('min_capacity', ve.error_dict)

	def test_parking_capacity_trows_error_when_cero_is_given(self):
		place = self.place_cretator()
		place.parking_capacity = 0
		self.assertRaises(ValidationError, place.clean_fields)
		try:
			place.clean_fields()
		except ValidationError as ve:
			self.assertIn('parking_capacity', ve.error_dict)

	def test_parking_capacity_trows_error_when_negative_number_is_given(self):
		place = self.place_cretator()
		place.parking_capacity = -1
		self.assertRaises(ValidationError, place.clean_fields)
		try:
			place.clean_fields()
		except ValidationError as ve:
			self.assertIn('parking_capacity', ve.error_dict)

	def test_kitchen_sqrt_m_trows_error_when_cero_is_given(self):
		place = self.place_cretator()
		place.kitchen_sqrt_m = 0 
		self.assertRaises(ValidationError, place.clean_fields)
		try:
			place.clean_fields()
		except ValidationError as ve:
			self.assertIn('kitchen_sqrt_m', ve.error_dict)

	def test_kitchen_sqrt_m_trows_error_when_negative_number_is_given(self):
		place = self.place_cretator()
		place.kitchen_sqrt_m = -1
		self.assertRaises(ValidationError, place.clean_fields)
		try:
			place.clean_fields()
		except ValidationError as ve:
			self.assertIn('kitchen_sqrt_m', ve.error_dict)

	def test_last_modified_field_sotres_the_date_for_the_las_modification(self):
		place = self.place_cretator()
		place.save()
		place.ac = True
		place.save()
		self.assertEqual(place.last_modified, date.today())

	def test_str_representation_of_place_instance_is_name_plus_pk(self):
		place = self.place_cretator()
		place.name = 'Salon'
		place.save()
		self.assertEqual(str(Place.objects.get(name='Salon')), place.name+'-'+str(place.pk))

	def test_default_value_for_active_dield_is_true(self):
		place = Place()
		self.assertTrue(place.active)


#Form created for testing model options is rendered as a select widget
class RegionForm(ModelForm):
	class Meta:
		model = Region
		fields = '__all__'

class RegionTest(TestCase):

	def test_region_model_can_store_in_the_database_the_correct_data(self):
		region = Region(region='Estado de Mexico')
		region.save()
		self.assertEqual(Region.objects.count(), 1)

	def test_region_field_is_rendered_as_a_select_type(self):
		region = RegionForm()
		self.assertIsInstance(region.fields['region'].widget, Select)


#Form created for testing model options is rendered as a select widget
class LocalityForm(ModelForm):
	class Meta:
		model = Locality
		fields = '__all__'

class LocalityTest(TestCase):
	fixtures = ['region_foreign_key_fixture']

	def test_locality_model_can_store_in_the_database_the_correct_data(self):
		locality = Locality(
			locality='Metepec',
			region=Region.objects.get(pk=1)
			)
		locality.save()
		self.assertEqual(Locality.objects.count(), 1)

	def test_state_field_is_rendered_as_a_select_type(self):
		locality = LocalityForm()
		self.assertIsInstance(locality.fields['locality'].widget, Select)


class AddressTest(TestCase):
	fixtures = ['place_foreign_key_fixture', 'locality_foreign_key_fixture']

	def address_cretator(self):
		data = {
			'address_line_1': 'Place street, Place number',
			'address_line_2': 'Place inside number',
			'address_line_3': 'Place colonia',
			'postal_code': '52176',
			'locality': Locality.objects.get(pk=1),
			'place': Place.objects.get(pk=1)
		}
		address = Address(**data)
		return address

	def test_address_model_can_store_in_the_database_the_correct_data(self):
		address = self.address_cretator()
		address.save()
		self.assertEqual(Address.objects.count(), 1)

	def test_some_address_model_fields_can_accept_blank_values(self):
		place = Place.objects.get(pk=1)
		address = Address(
			address_line_1='Place street, Place number',
			address_line_2='',
			address_line_3='',
			postal_code='',
			locality=Locality.objects.get(pk=1),
			place=Place.objects.get(pk=1)
		)
		address.save()
		self.assertEqual(Address.objects.count(), 1)

	def test_address_gets_deleted_when_foreign_key_is_deleted(self):
		address = self.address_cretator()
		address.save()
		self.assertEqual(Address.objects.count(), 1)
		Place.objects.get(pk=1).delete()
		self.assertEqual(Address.objects.count(), 0)

	def test_str_representation_of_address_model_is_foreign_key_str(self):
		address = self.address_cretator()
		address.save()
		self.assertEqual('Uno-1',str(address))


	def test_there_is_only_one_address_per_model(self):
		address = self.address_cretator()
		address.save()
		address_2 = Address(
			address_line_1='Place street, Place number',
			address_line_2='Place inside number',
			address_line_3='Place colonia',
			postal_code='',
			locality=Locality.objects.get(pk=1),
			place=Place.objects.get(pk=1)
		)
		self.assertRaises(ValidationError, address_2.full_clean)
		try:
			address_2.full_clean()
		except ValidationError as ve:
			self.assertIn('place', ve.error_dict)

	def test_place_field_is_primary_key_of_address_model(self):
		address = self.address_cretator()
		address.save()
		self.assertEqual(address.pk, Place.objects.get(pk=1).pk)



#Form created for testing model options is rendered as a select widget
class TelephoneForm(ModelForm):
	class Meta:
		model = Telephone
		fields = '__all__'


class TelephoneTest(TestCase):
	fixtures = ['place_foreign_key_fixture']

	def phone_cretator(self):
		data = {
			'number': '1234567890',
			'phone_type': 'cell',
			'place': Place.objects.get(pk=1)
		}
		phone = Telephone(**data)
		return phone

	def test_telephone_model_can_store_in_the_database_the_correct_data(self):
		phone = self.phone_cretator()
		phone.save()
		self.assertEqual(Telephone.objects.count(), 1)

	def test_telephone_gets_deleted_when_foreign_key_is_deleted(self):
		phone = self.phone_cretator()
		phone.save()
		self.assertEqual(Telephone.objects.count(), 1)
		Place.objects.get(pk=1).delete()
		self.assertEqual(Telephone.objects.count(), 0)

	def test_telephone_get_validated_for_less_than_ten_numbers(self):
		phone = self.phone_cretator()
		phone.number='123456789'
		self.assertRaises(ValidationError, phone.clean_fields)
		try:
			phone.clean_fields()
		except ValidationError as ve:
			self.assertIn('number', ve.error_dict)

	def test_telephone_get_validated_for_more_than_ten_numbers(self):
		phone = self.phone_cretator()
		phone.number='12345678901'
		self.assertRaises(ValidationError, phone.clean_fields)
		try:
			phone.clean_fields()
		except ValidationError as ve:
			self.assertIn('number', ve.error_dict)

	def test_telephone_get_validated_for_having_only_numbers(self):
		phone = self.phone_cretator()
		phone.number='123456789O'								#The las digit is "O" not a cero
		self.assertRaises(ValidationError, phone.clean_fields)
		try:
			phone.clean_fields()
		except ValidationError as ve:
			self.assertIn('number', ve.error_dict)

	def test_str_representation_of_telephone_model_is_foreign_key_str_plus_four_last_digits(self):
		phone = self.phone_cretator()
		phone.number='9876543210'
		phone.save()
		self.assertEqual('Uno-1-3210',str(phone))

	def test_phone_field_is_rendered_as_a_select_type(self):
		phone = TelephoneForm()
		self.assertIsInstance(phone.fields['phone_type'].widget, Select)


class EmailTest(TestCase):
	fixtures = ['place_foreign_key_fixture']

	def email_creator(self):
		place = Place.objects.get(pk=1)
		email = Email(
			email='beto@test.com',
			place=Place.objects.get(pk=1)
		)
		email.save()
		return email

	def test_email_model_can_store_in_the_database_the_correct_data(self):
		email = self.email_creator()
		self.assertEqual(Email.objects.count(), 1)

	def test_email_gets_deleted_when_foreign_key_is_deleted(self):
		email = self.email_creator()
		self.assertEqual(Email.objects.count(), 1)
		Place.objects.get(pk=1).delete()
		self.assertEqual(Email.objects.count(), 0)


	def test_str_representation_of_email_instance_is_email(self):
		email = self.email_creator()
		self.assertEqual(str(Email.objects.get(email='beto@test.com')),'beto@test.com')


class RepresentativeTest(TestCase):
	fixtures = ['place_foreign_key_fixture']

	def representative_creator(self):
		place = Place.objects.get(pk=1)
		representative = Representative(
			representative='Carlos Alberto Hurtado',
			place=Place.objects.get(pk=1)
		)
		representative.save()
		return representative

	def test_repersentative_model_can_store_in_the_database_the_correct_data(self):
		representative = self.representative_creator()
		self.assertEqual(Representative.objects.count(), 1)

	def test_repersentative_gets_deleted_when_foreign_key_is_deleted(self):
		representative = self.representative_creator()
		self.assertEqual(Representative.objects.count(), 1)
		Place.objects.get(pk=1).delete()
		self.assertEqual(Representative.objects.count(), 0)

	def test_str_representation_of_representative_instance_is_representaive_plus_place(self):
		representative = self.representative_creator()
		self.assertEqual(str(Representative.objects.get(representative='Carlos Alberto Hurtado')),
			'Carlos Alberto Hurtado'
		)


class SocialMediaTest(TestCase):
	fixtures = ['place_foreign_key_fixture']

	def social_media_creator(self):
		place = Place.objects.get(pk=1)
		social_media = SocialMedia(
			social_media='https://www.facebook.com/salon',
			place=Place.objects.get(pk=1)
		)
		social_media.save()
		return social_media

	def test_social_media_model_can_store_in_the_database_the_correct_data(self):
		social_media = self.social_media_creator()
		self.assertEqual(SocialMedia.objects.count(), 1)

	def test_social_media_gets_deleted_when_foreign_key_is_deleted(self):
		social_media = self.social_media_creator()
		self.assertEqual(SocialMedia.objects.count(), 1)
		Place.objects.get(pk=1).delete()
		self.assertEqual(SocialMedia.objects.count(), 0)

	def test_str_representation_of_representative_instance_is_representaive_plus_place(self):
		social_media = self.social_media_creator()
		self.assertEqual(str(SocialMedia.objects.get(social_media='https://www.facebook.com/salon')),
			'www.facebook.com'
		)


class ProfilePictureTest(TestCase):
	fixtures = ['place_foreign_key_fixture']

	def profile_picture_creator(test):
		def create_profile_picture(self):
			with open(PICTURES_PATH+'Test_Profile_1.png', 'r+b') as img:
				profile_picture = ProfilePicture(
					picture=ImageFile(img),
					place=Place.objects.get(pk=1)
				)
				test(self, profile_picture)
		return create_profile_picture

	@profile_picture_creator
	def test_profile_picure_model_can_store_in_the_database_the_correct_data(self, profile_picture):
		profile_picture.save()
		self.assertEqual(ProfilePicture.objects.count(), 1)
			
	@profile_picture_creator
	def test_profile_pictures_are_upladed_to_the_correct_path(self, profile_picture):
		profile_picture.save()
		self.assertTrue(os.path.isfile(MEDIA_URL+str(profile_picture.picture)))

	@profile_picture_creator
	def test_there_is_only_one_profile_picture_per_model(self, profile_picture):
		profile_picture.save()
		with open(PICTURES_PATH+'Test_Profile_2.png', 'r+b') as img:
			profile_picture_2 = ProfilePicture(
				picture=ImageFile(img),
				place=Place.objects.get(pk=1)
			)
			self.assertRaises(ValidationError, profile_picture_2.full_clean)
			try:
				profile_picture_2.full_clean()
			except ValidationError as ve:
				self.assertIn('place', ve.error_dict)

	@profile_picture_creator
	def test_profile_picture_gets_deleted_when_foreign_key_is_deleted(self, profile_picture):
		profile_picture.save()
		self.assertEqual(ProfilePicture.objects.count(), 1)
		Place.objects.get(pk=1).delete()
		self.assertEqual(ProfilePicture.objects.count(), 0)

	@profile_picture_creator
	def test_place_field_is_primary_key_of_profile_picture_model(self, profile_picture):
		profile_picture.save()
		self.assertEqual(profile_picture.pk, Place.objects.get(pk=1).pk)

	@profile_picture_creator
	def test_str_representation_of_profile_picture_model_is_foreign_key_str(self, profile_picture):
		profile_picture.save()
		self.assertEqual('Uno-1', str(profile_picture))


class PictureTest(TestCase):
	fixtures = ['place_foreign_key_fixture']

	def picture_creator(test):
		def create_picture(self):
			with open(PICTURES_PATH+'Test_1.png', 'r+b') as img_1:
				picture = Picture(
					picture=ImageFile(img_1),
					place=Place.objects.get(pk=1)
				)
				test(self, picture)
		return create_picture

	@picture_creator
	def test_picure_model_can_store_in_the_database_the_correct_data(self, picture):
		picture.save()
		self.assertEqual(Picture.objects.count(), 1)
	
	@picture_creator
	def test_pictures_are_upladed_to_the_correct_path(self, picture):
		picture.save()
		self.assertTrue(os.path.isfile(MEDIA_URL + str(picture.picture)))

	@picture_creator
	def test_picture_gets_deleted_when_foreign_key_is_deleted(self, picture):
		picture.save()
		self.assertEqual(Picture.objects.count(), 1)
		Place.objects.get(pk=1).delete()
		self.assertEqual(Picture.objects.count(), 0)