from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from example.forms import GiftListForm
from example.models import GiftList


def hello_world(request):
    return HttpResponse("Hello World!")


def hello_name(request, name):
    return HttpResponse(f"Hello, {name}!")


def hello_world_template(request):
    return render(request, "index.html", {})


def simple_list_view(request):
    gfl_entries = GiftList.objects.all()
    return render(request, "list.html", {"gfl_entries": gfl_entries})


class GiftListListView(ListView):
    model = GiftList
    template_name = "list.html"
    context_object_name = "gfl_entries"


class PostCreateView(CreateView):
    model = GiftList
    form_class = GiftListForm
    success_url = "/gift_list/add"
    template_name = "add.html"
