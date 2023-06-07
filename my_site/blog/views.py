import random
import time

from django.views.decorators.cache import cache_page
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from faker import Faker

from .models import Blog


def index(request):
    return HttpResponse({"Main Page"})


def create_blog(request):
    faker = Faker()
    title = faker.word()
    content = faker.text()
    blog = Blog.objects.create(title=title, content=content)
    create_blog = Blog.objects.all()
    return render(request, "create_blog.html", {"create_blog": create_blog})


@cache_page(60 * 15)
def get_blog(request, id):
    blog = Blog.objects.get(id=id)
    print("waiting")
    time.sleep(4)
    return render(request, "get_blog.html", {"blog": blog})


def update(request, id):
    blog = Blog.objects.get(id=id)
    blog.title = "some title"
    blog.save()
    return redirect("get_blog", id=id)
