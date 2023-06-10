from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy 
# Create your views here idiot.


class ProjectHomePage(TemplateView):
    template_name = "home.html"

class ProjectEditView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["tittle", "body"]

class ProjectDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")