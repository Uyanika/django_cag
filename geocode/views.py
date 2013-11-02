# Create your views here.
from models import *
from django.shortcuts import render_to_response
def index(request):

    #print destinations
    return render_to_response('index.html')

def search(request):
    if 'destination' in request.GET:
        param = request.GET['destination']
        destinations = Destinations.objects.filter(cityname__contains = param)
        #destinations = Destinations.objects.all()
        return render_to_response('search.html', {'param':param, 'destinations': destinations})
