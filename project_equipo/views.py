<<<<<<< HEAD
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post

=======
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy 
>>>>>>> b9f20d8785654dd7a4e924f18cff01b153b29448
# Create your views here idiot.
class ProjectHomePage(TemplateView):
    template_name = "home.html"

<<<<<<< HEAD
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
=======
class ProjectEditView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["tittle", "body"]

class ProjectDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
>>>>>>> b9f20d8785654dd7a4e924f18cff01b153b29448
