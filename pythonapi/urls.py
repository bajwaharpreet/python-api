from django.urls import path
from pythonapi import views


urlpatterns = [
   path("home", views.first_api)
]