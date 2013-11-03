# Create your views here.
from models import *
from geocode_hesap import geocode_hesap
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
def calculate_route(request):
    nereden = None
    nereye = None
    if 'nereden' in request.GET:
        nereden = request.GET['nereden']
        nereden = geocode_hesap(nereden)
    if 'nereye' in request.GET:
        nereye = request.GET['nereye']
        nereye = geocode_hesap(nereye)
    return render_to_response('calculate_route.html', {'nereden':nereden, 'nereye': nereye } )

