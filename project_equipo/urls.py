from django.urls import path
from .views import ProjectHomePage

urlpatterns = [
    path("", ProjectHomePage.as_view(), name="home")
]