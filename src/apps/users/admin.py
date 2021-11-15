from django.contrib import admin

# Register your models here.
from src.apps.users.models import User

admin.site.register(User)
