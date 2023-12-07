from django.urls import path
from . import views


urlpatterns = [
    path("first_view/", views.home_view, name="home_view")
]
