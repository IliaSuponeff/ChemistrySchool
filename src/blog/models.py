from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	link = models.CharField(max_length=200)
	publication_date = models.DateTimeField()
