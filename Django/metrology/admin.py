from django.contrib import admin

from .models import Metrology, Offers

class MetrologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'organisation', 'name_SI', 'registration_number', 'data_Power', 'photo')
    list_display_links = ('id', 'organisation')
    search_fields = ('id', 'organisation', 'name_SI', 'registration_number', 'data_Power')

class OffersAdmin(admin.ModelAdmin):
    list_display = ('id', 'organisation', 'is_published')
    list_display_links = ('id', 'organisation')
    search_fields = ('id', 'organisation', 'is_published')

admin.site.register(Metrology, MetrologyAdmin)
admin.site.register(Offers, OffersAdmin)