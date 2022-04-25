from django.db import models 
#from mapbox_location_field.models import LocationField
#import punkt.mqtt as mqtt
#import datetime
#from django.utils import timezone

# Create your models here.

class Punkt(models.Model):
    punkt_text = models.CharField(max_length=200)
    punkt_oppdatert = models.DateTimeField('date updated')
    def __str__(self):
        return self.punkt_text

    

class Measurement(models.Model):
    punkt = models.ForeignKey(Punkt, on_delete=models.CASCADE)
    measurement_text = models.CharField(max_length=200)
    #measure = models.IntegerField(default=0)
    def __str__(self):
        return self.measurement_text



    

    
    
    