import datetime

from django.db import models
from django.utils import timezone


class Post(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	link = models.CharField(max_length=200)
	publication_date = models.DateTimeField(auto_now_add=True)

	def __str__(self) -> str:
		args = [
			f"id={self.id}",
			f"title={self.title}",
			f"descripton={self.description[:50]}",
			f"link={self.link}",
			f"date={self.publication_date}"
		]
		return f"<{self.__class__.__name__}: {' '.join(args)}>"
	
	def __repr__(self) -> str:
		return self.__str__()
	
	def was_published_recently(self)-> bool:
		return self.publication_date >= timezone.now() - datetime.timedelta(days=1)
	