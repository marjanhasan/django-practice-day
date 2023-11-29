from django.urls import path
from . import views

urlpatterns = [
    path("", views.navigation),
    path("about/", views.about),
    path("contact/", views.contact),
]
