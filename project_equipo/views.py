from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post

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