from django.contrib import admin

from places.forms import PlacesForm
from places.models import Place, Address, Telephone, Email, Representative, SocialMedia, ProfilePicture, Picture


class AddressInline(admin.StackedInline):
	model = Address
	extra = 1

class TelephoneInline(admin.TabularInline):
	model = Telephone
	extra = 2

class EmailInline(admin.TabularInline):
	model = Email
	extra = 1

class RepresentativeInline(admin.TabularInline):
	model = Representative
	extra = 1

class SocialMediaInline(admin.TabularInline):
	model = SocialMedia
	extra = 3

class ProfilePictureInline(admin.TabularInline):
	model = ProfilePicture
	extra = 1

class PictureInline(admin.TabularInline):
	model = Picture
	extra = 5

class PlacesAdmin(admin.ModelAdmin):
	inlines = [
		AddressInline,
		TelephoneInline,
		EmailInline,
		RepresentativeInline,
		SocialMediaInline,
		ProfilePictureInline,
		PictureInline
	]
	form = PlacesForm

admin.site.register(Place, PlacesAdmin)
