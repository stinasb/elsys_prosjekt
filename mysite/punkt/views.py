from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
#from django.template import loader

from .models import Measurement, Punkt


def index(request):
    punkt_liste = Punkt.objects.all()
    measurement_liste = Measurement.objects.all()
    #template = loader.get_template('punkt/index.html')
    context = {
        'punkt_liste': punkt_liste, 
        'measurement_liste' : measurement_liste,
    }
    #output = ', '.join([p.punkt_text for p in punkt_liste])
    #return HttpResponse(template.render(context, request))
    return render(request, 'punkt/index.html', context)



def detail(request, punkt_id):
    #try:
     #   punkt = Punkt.objects.get(pk=punkt_id)
    #except Punkt.DoesNotExist:
     #   raise Http404("Punkt finnes ikke")
    #return HttpResponse("Du ser paa %s." % punkt_id)
    punkt = get_object_or_404(Punkt, pk = punkt_id)
    return render(request, 'punkt/detail.html', {'punkt':punkt})


