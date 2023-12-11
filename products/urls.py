from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("<slug:cat_slug>/", views.home_view, name="home_view")
]
