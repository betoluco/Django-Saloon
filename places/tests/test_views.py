from django.test import TestCase

from places.models import Place

class HomePageTest(TestCase):
	fixtures = ['home_page_fixtures']

	def test_home_page_renders_home_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'places/home_page.html')

	def test_results_view_queries_all_active_markers_in_the_boundaries_passed_in_URL(self):
		response = self.client.get('/results/?bounds={%22south%22:19.237373, %22west%22:-99.746390, %22north%22:19.410055, %22east%22:-99.520312}')
		self.assertEqual(len(response.context['markers']), 12)
		objects = (Place.objects.get(pk=1), Place.objects.get(pk=2), Place.objects.get(pk=3))
		for obj in objects:
			self.assertNotIn(obj, response.context['markers'])

	def test_results_view_returns_places_in_groups_of_ten_elements(self):
		response = self.client.get('/results/?bounds={%22south%22:19.237373, %22west%22:-99.746390, %22north%22:19.410055, %22east%22:-99.520312}')
		self.assertEqual(len(response.context['results']), 10)
	
	def test_results_view_returns_page_one_if_no_page_paremter_is_provided_in_the_url(self):
		response = self.client.get('/results/?bounds={%22south%22:19.237373, %22west%22:-99.746390, %22north%22:19.410055, %22east%22:-99.520312}')
		objects = (Place.objects.get(pk=4), Place.objects.get(pk=5), Place.objects.get(pk=6),\
			Place.objects.get(pk=7), Place.objects.get(pk=8), Place.objects.get(pk=9),\
			Place.objects.get(pk=10), Place.objects.get(pk=11), Place.objects.get(pk=12),\
			Place.objects.get(pk=13))
		print(response.context['results'].object_list)
		for obj in objects:
			self.assertIn(obj, response.context['results'].object_list)

	def test_results_view_returns_the_page_selected_through_a_keyword_argument_passed_in_the_url(self):
		response = self.client.get('/results/?bounds={%22south%22:19.237373, %22west%22:-99.746390, %22north%22:19.410055, %22east%22:-99.520312}&page=2')
		self.assertEqual(len(response.context['results']), 2)
		objects = (Place.objects.get(pk=14), Place.objects.get(pk=15))
		for obj in objects:
			self.assertIn(obj, response.context['results'].object_list)

	def test_place_view_returns_place_requested_in_the_url(self):
		response = self.client.get('/place/?place=4')
		self.assertEqual(Place.objects.get(pk=4), response.context['place'])
