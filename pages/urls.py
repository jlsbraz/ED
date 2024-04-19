from django.urls import path
from .views import homePagesView

urlpatterns = [
    path("", homePagesView, name="home"),
]