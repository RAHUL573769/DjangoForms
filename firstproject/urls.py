from django.contrib import admin
from django.urls import path

from django.urls import include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homepage),
    path("first/", include("firstapp.urls")),
]
