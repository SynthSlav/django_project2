from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method == 'POST':
        return HttpResponse("Hello, World! This is the index page of our Django application.")
    else:
        return HttpResponse(request.method)