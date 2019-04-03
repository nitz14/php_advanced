from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from example.forms import GiftForm, GiftListForm
from example.models import Gift, GiftList


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


class PostEditView(UpdateView):
    model = GiftList
    form_class = GiftListForm
    template_name = "add.html"

    @property
    def success_url(self):
        return reverse("list_gfl")


class PostDeleteView(DeleteView):
    model = GiftList
    template_name = "delete.html"

    @property
    def success_url(self):
        return reverse("list_gfl")


class PostCreateGiftView(CreateView):
    model = Gift
    form_class = GiftForm
    success_url = "/gift/add"
    template_name = "add.html"


class PostEditGiftView(UpdateView):
    model = Gift
    form_class = GiftForm
    template_name = "add.html"

    @property
    def success_url(self):
        return reverse("list_gfl")


class PostDeleteGiftView(DeleteView):
    model = Gift
    template_name = "delete.html"

    @property
    def success_url(self):
        return reverse("list_gfl")
