from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

""" Each function is a view that will render different html templates / Vue templates"""

def home(request):
    return render(request, 'fetch_api_app/main.html')
