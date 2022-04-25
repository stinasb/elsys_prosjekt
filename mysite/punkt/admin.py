from django.contrib import admin

# Register your models here.
from .models import Punkt, Measurement

admin.site.register(Punkt)
admin.site.register(Measurement)