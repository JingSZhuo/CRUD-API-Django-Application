from django.contrib import admin

# Register your models here.

from .models import *

""" Allows modification in the admin panel"""
admin.site.register(FormQuestions)