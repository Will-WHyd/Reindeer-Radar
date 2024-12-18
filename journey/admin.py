from django.contrib import admin
from .models import Household, Kid

# Register your models here.
@admin.register(Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'city', 'visited')
    list_filter = ['user', 'name', 'city', 'visited']
    search_fields = ['user', 'name']


@admin.register(Kid)
class KidAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'family', 'behavior')
    list_filter = ['user', 'name', 'family', 'behavior']
    search_fields = ['user', 'name', 'family']