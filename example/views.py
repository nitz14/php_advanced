from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return HttpResponse("Hello World!")


def hello_name(request, name):
    return HttpResponse(f"Hello, {name}!")


def hello_world_template(request):
    return render(request, "index.html", {})
