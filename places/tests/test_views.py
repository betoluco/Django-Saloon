from django.test import TestCase

from places.models import Place

class HomePageTest(TestCase):
	fixtures = ['home_page_fixtures']

	def test_home_page_renders_home_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'places/home_page.html')

	def test_home_page_query_all_active_places(self):
		response = self.client.get('/')
		self.assertNotIn(Place.objects.get(pk=1), response.context['places'])

	def test_results_view_queries_are_diplayed_in_groups_of_five_elements(self):
		response = self.client.get('/results/?bounds={%22south%22:20, %22west%22:-100, %22north%22:19, %22east%22:-99}')
		self.assertEqual(len(response.context['results']), 5)

	def test_results_view_queries_for_active_places_in_the_boundaries_passed_in_URL(self):
		response = self.client.get('/results/?bounds={%22south%22:19.237373, %22west%22:-99.746390, %22north%22:19.410055, %22east%22:-99.520312}')
		self.assertEqual(len(response.context['results']), 4)
		objects = (Place.objects.get(pk=1), Place.objects.get(pk=2), Place.objects.get(pk=3))
		for obj in objects:
			self.assertNotIn(obj, response.context['results'])
	
	def test_the_group_displayed_is_selected_through_a_keyword_argument_passed_in_the_url(self):
		response = self.client.get('/results/?bounds={%22south%22:20, %22west%22:-100, %22north%22:19, %22east%22:-99}&page=2')
		self.assertIn(Place.objects.get(pk=7), response.context['results'])

	def test_if_the_keyword_argument_passed_in_the_url_is_not_an_intege_the_first_page_is_returned(self):
		response = self.client.get('/results/?bounds={%22south%22:20, %22west%22:-100, %22north%22:19, %22east%22:-99}&page=None')
		objects = [
			Place.objects.get(pk=2),
			Place.objects.get(pk=3),
			Place.objects.get(pk=4),
			Place.objects.get(pk=5),
			Place.objects.get(pk=6)
			]
		self.assertListEqual(objects, response.context['results'].object_list)