from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
import time
from django.contrib.auth.models import User


class AdminTest(FunctionalTest):
	
	def test_admin_can_create_new_element_and_it_is_displayed_on_the_map(self):
		super_user = User.objects.create_user("Beto", password="caf5tl00")
		super_user.is_superuser = True
		super_user.is_staff = True
		super_user.save()
		# An Administrator opens the admin places add page
		self.browser.get(self.server_url+'/admin')
		# enters his username
		form_username = self.browser.find_element_by_id('id_username')
		form_username.send_keys('Beto')
		# enters his password
		form_password = self.browser.find_element_by_id('id_password')
		form_password.send_keys('caf5tl00')
		# and enters the Django admin
		form_password.send_keys(Keys.RETURN)
		# he navigates the page to get to the form to add a new place
		self.browser.find_element_by_xpath('//a[contains(@href, "place/add")]').click()
		#he add a new place 

		# And saves the model
		self.browser.find_element_by_name('_save').click()
		# Goes to the main page to check that the new element was added to the map
		self.browser.get(self.server_url)
		# Veryfy that the point was added
		time.sleep(10)

class VisitorTest(FunctionalTest):
	fixtures = ['home_page_fixtures']

	def test_user_can_search_in_the_map(self):
		self.browser.get(self.server_url)
		time.sleep(30)
		