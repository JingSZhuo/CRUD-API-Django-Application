from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from fetch_api_app.models import FormQuestions

import json

# Create your views here.

""" Each function is a view that will render different html templates or HTTP/JSON Responses"""

def home(request):
    return render(request, 'fetch_api_app/main.html')


"""Creates a list of dictionaries via the []"""
#view function that returns a JSONResponse

"""
    CSRF Exempt for the form_api function to enable data write to the Models database

    Each method returns a JsonResponse as a HttpResponse, this serves as the API between the front end and the DB 

"""

@csrf_exempt
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
        json_convert_to_dictionary = json.loads(request.body)
        new_form_data = FormQuestions.objects.create(
            email = json_convert_to_dictionary['email'] ,
            username = json_convert_to_dictionary['username'],
            age = json_convert_to_dictionary['age'],
            date_posted = json_convert_to_dictionary['date'],
        )
        return JsonResponse(new_form_data.to_dictionary())

    elif request.method == 'PUT':
        json_convert_to_dictionary = json.loads(request.body)
        identifier = json_convert_to_dictionary['id_edit']

        getId = FormQuestions.objects.get(pk=identifier)

        getId.email = json_convert_to_dictionary['updated_email']
        getId.username = json_convert_to_dictionary['updated_username']
        getId.age = json_convert_to_dictionary['updated_age']
        getId.date_posted = json_convert_to_dictionary['updated_date']
        getId.save()

        return JsonResponse({ 
            'forms_dictionary' : [
                data.to_dictionary()
                for data in FormQuestions.objects.all()
                ]
            })

    elif request.method == 'DELETE':
        json_convert_to_dictionary = json.loads(request.body)
        identifier = json_convert_to_dictionary['id']

        getId = FormQuestions.objects.get(pk=identifier)
        getId.delete()
        return JsonResponse({ 
            'forms_dictionary' : [
                data.to_dictionary()
                for data in FormQuestions.objects.all()
                ]
            })
    else: 
        pass

    