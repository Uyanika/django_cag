# Create your views here.
 # -*- coding: UTF-8 -*-
from models import *
from geocode_hesap import geocode_hesap
from django.shortcuts import render_to_response
from httplib import HTTPResponse
import json, autocomplete_light
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
def calculate_directions(request):
    return render_to_response('calculate_directions.html')
def calculate_route_directions(request):
    return render_to_response('calculate_route_directions.html')
def merhaba(request):
    return render_to_response('merhaba.html')
def ara(request):
    nereden = request.GET['term']
    return HTTPResponse(json.dumps(None), content_type="application/json")
