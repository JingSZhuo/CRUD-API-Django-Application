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
    
    """Converts database object to dictionary (JSON Format)"""
    
    def to_dictionary(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'age': self.age,
            'date_posted': self.date_posted,
        }
    
    