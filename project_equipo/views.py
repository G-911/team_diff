from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Post
from django.urls import reverse_lazy 
# Create your views here idiot.

class ProjectHomePage(TemplateView):
    template_name = "home.html"

class ProjectListView(ListView):
    model = Post
    template_name = "home.html"

class ProjectCreateView(CreateView):
    model = Post
    template_name = "NewPost.html"
    fields = ["title", "body", "author"]

class ProjectDetailView(DetailView):
    model = Post
    template_name = "DetailPost.html"

class ProjectEditView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["tittle", "body"]

class ProjectDeleteView(DeleteView):
    model = Post
    template_name = "delete_project.html"
    success_url = reverse_lazy("home")
