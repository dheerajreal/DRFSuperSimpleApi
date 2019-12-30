from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    date_created = models.DateField(auto_now=True, auto_now_add=False)
