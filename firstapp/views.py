from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage1(request):
    return render(request, "about.html")
