from django.test import TestCase

from places.models import Place

class HomePageTest(TestCase):
	fixtures = ['home_page_fixtures']

	def test_home_page_query_all_active_places(self):
		response = self.client.get('/')
		self.assertEqual(len(response.context['places']), 4)

	def test_results_queries_for_active_places_in_the_boundaries_passed_in_URL(self):
		response = self.client.get('/results/?swLat=-19.237373&swLng=-99.746390&neLat=19.410055&neLng=-99.520312')
		self.assertEqual(len(response.context['results']), 2)
