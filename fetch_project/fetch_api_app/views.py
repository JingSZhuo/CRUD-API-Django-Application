from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from fetch_api_app.models import FormQuestions

# Create your views here.

""" Each function is a view that will render different html templates / Vue templates"""

def home(request):
    return render(request, 'fetch_api_app/main.html')


"""Creates a list of dictionaries via the []"""
#view function that returns a JSONResponse

def form_api(request):              #GET request of the database object model
    if request.method == 'GET':
        return JsonResponse({
            'forms_dictionary' : [
                data.to_dictionary()
                for data in FormQuestions.objects.all()
            ]
        })
    elif request.method == 'POST':
        #create new recipe (list) -> then create new recipe object then convert to JSON
        new_form_data = FormQuestions.objects.create(
            email = "test2@gmail.com",
            username = "someUserName...",
            age = "40",
            date_posted = "",
        )
        return JsonResponse(new_form_data.to_dictionary())
        

    