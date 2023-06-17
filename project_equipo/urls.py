from django.urls import path
<<<<<<< HEAD
from .views import ProjectHomePage, ProjectDetailView, ProjectCreateView, ProjectListView

urlpatterns = [
    path("", ProjectHomePage.as_view(), name="home"),
    path("post/new/", ProjectCreateView.as_view(), name="post_new"),
    path("post/<int:pk>", ProjectDetailView.as_view(), name="post_detail"),
    path("", ProjectListView.as_view(), name="home"),

=======
from .views import ProjectHomePage, ProjectDeleteView, ProjectEditView

urlpatterns = [
    path("", ProjectHomePage.as_view(), name="home"),
    path("post/<int:pk>/edit/", ProjectEditView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", ProjectDeleteView.as_view(), name="post_delete"),
>>>>>>> b9f20d8785654dd7a4e924f18cff01b153b29448
]