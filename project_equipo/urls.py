from django.urls import path
from .views import ProjectHomePage, ProjectDeleteView, ProjectEditView

urlpatterns = [
    path("", ProjectHomePage.as_view(), name="home"),
    path("post/<int:pk>/edit/", ProjectEditView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", ProjectDeleteView.as_view(), name="post_delete"),
]