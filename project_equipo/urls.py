from django.urls import path
from .views import ProjectHomePage, ProjectDetailView, ProjectCreateView, ProjectListView, ProjectEditView, ProjectDeleteView

urlpatterns = [
    path("", ProjectHomePage.as_view(), name="home"),
    path("post/new/", ProjectCreateView.as_view(), name="NewPost"),
    path("post/<int:pk>", ProjectDetailView.as_view(), name="DetailPost"),
    path("", ProjectListView.as_view(), name="home"),
    path("post/<int:pk>/edit/", ProjectEditView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", ProjectDeleteView.as_view(), name="delete_project"),
]