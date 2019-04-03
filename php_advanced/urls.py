"""php_advanced URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from example import views as example_views

urlpatterns = [
    url(r"^hello$", example_views.hello_world),
    url(r"^hello/(?P<name>\w+)$", example_views.hello_name),
    url(r"^hello_template$", example_views.hello_world_template),
    url(r"^gift_list_by_func_view/$", example_views.simple_list_view),
    url(
        r"^gift_list_by_class_view/$",
        example_views.GiftListListView.as_view(),
        name="list_gfl",
    ),
    url(r"^gift_list/add/$", example_views.PostCreateView.as_view()),
    url(
        r"^gift_list/edit/(?P<pk>\d+)/$",
        example_views.PostEditView.as_view(),
        name="edit_gfl",
    ),
    url(r"^admin/", admin.site.urls),
]
