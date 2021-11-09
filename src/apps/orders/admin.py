from django.contrib import admin

# Register your models here.
from src.apps.orders.models import Order

admin.site.register(Order)
