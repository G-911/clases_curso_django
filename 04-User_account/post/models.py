from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    auth = models.ForeignKey("auth.User", on_delete=models.CASCADE,)

    def str(self):
        return self.title