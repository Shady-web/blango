from django.shortcuts import render
import requests
# Create your views here.
def index(request):
  return render(request, "blog/index.html")