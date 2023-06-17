from django.urls import path
from .views import ProjectHomePage, ProjectDetailView, ProjectCreateView, ProjectListView

urlpatterns = [
    path("", ProjectHomePage.as_view(), name="home"),
    path("post/new/", ProjectCreateView.as_view(), name="post_new"),
    path("post/<int:pk>", ProjectDetailView.as_view(), name="post_detail"),
    path("", ProjectListView.as_view(), name="home"),

]