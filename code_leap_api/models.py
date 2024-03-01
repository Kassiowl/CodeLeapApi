from django.db import models


class ContentModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=250)
    author = models.CharField(max_length=70)
    creation_date = models.DateField()