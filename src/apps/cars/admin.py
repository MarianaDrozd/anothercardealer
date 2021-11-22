from django.contrib import admin

# Register your models here.
from src.apps.cars.models import Car, Color, Brand, Model, Property, Picture, FuelType

admin.site.register(Car)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Property)
admin.site.register(Picture)
admin.site.register(FuelType)
