from django.urls import path
from . import views
from .views import LoginUser

app_name = "main"


urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name="register"),
    path('login/', LoginUser.as_view(), name='login'),
]
