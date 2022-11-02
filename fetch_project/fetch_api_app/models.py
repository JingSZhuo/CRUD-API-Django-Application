from django.db import models

# Create your models here.

""" 
    SQL Database Table Created with the name 'FormQuestions'  
    
    Each Table contains various fields each with their own different types 

"""

class FormQuestions(models.Model):
    email = models.EmailField(max_length=200 )
    username = models.CharField(max_length=200 )
    age = models.IntegerField(default=0 )
    date_posted = models.DateField('Date posted' )
    
    