from django.shortcuts import render
from django.http import HttpResponse

"""
TODO: Add view of add/edit post
TODO: Add view of representation of posts at db
"""


def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")
