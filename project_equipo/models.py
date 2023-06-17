from django.db import models
from django.urls import reverse


<<<<<<< HEAD
class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )

    body = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("DetailPost", kwargs={"pk": self.pk})
=======

class Post(models.Model):
    author = models.ForeignKey
>>>>>>> b9f20d8785654dd7a4e924f18cff01b153b29448
