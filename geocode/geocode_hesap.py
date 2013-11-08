__author__ = 'Arda'
 # -*- coding: UTF-8 -*-
__author__ = 'NAVM1'
import shapely.geometry
import pyproj
import math


from shapely.geometry import Point
import sqlite3 as lite

import json, urllib, urllib2
from pyproj import Proj
wgs84=pyproj.Proj("+init=EPSG:4326")
def drange(start, stop, step):
     r = start
     while r < stop:
         yield r
         r += step
def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return round(d)
def geocode_hesap(adres):
    call = lite.connect("C:\Projects\django_cag\destinations.sqlite")

    with call:
        cityName = adres
        curs = call.cursor()
        curs.execute("SELECT  Lat, Lon, CityName, Airport, Country FROM destinations WHERE CityName or Airport LIKE '%s' "%('%'+cityName+'%'))
        rows = curs.fetchall()
        coor = None
        if (len(rows) > 0):
            print #u"Aradığınız isme en uygun havaalanları:"
            i = 0
            for row in rows:
                i = i + 1
                print str(i) +' : ' + row[3] +' - ' + row[2] + ' , ' + row[4]
        print '----------------------------------'
        url="http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % urllib.quote(cityName)
        response = urllib2.urlopen(url)
        js_response = json.load(response)
        #print len(js_response['results'])
        if (len(js_response['results']) > 1):
            #print u"Adres tayini yapmaya çalışıyorum, birden fazla olasılık buldum:"
            i = 0
            coords = []
            for address in js_response['results']:
                coor = address['geometry']['location']
                coords.append(coor)
                i = i + 1
                print str(i) + ' : ' + address['formatted_address']
            secilen_adres = raw_input(u'Listeden  :')
            while (int(secilen_adres) > len(js_response['results']) or int(secilen_adres) < 0):
                secilen_adres = raw_input(u'Listeden  :')
            coor = coords[int(secilen_adres) - 1]
        else:
            coor = js_response['results'][0]['geometry']['location']
        if (coor != None):
            lat = coor['lat']
            lon = coor['lng']
            x, y = wgs84(lat, lon)

            target = Point(x, y)
            target1 = lat, lon
            #print target1
            
            curs.execute("SELECT  Lat, Lon, CityName, Airport, Country FROM destinations")
            rows = list(curs.fetchall())
            i = 0
            for x in drange(0,0.040,0.001): # yaklasik 250 km menzil/ 5 km artıs
                for row in rows:
                    x1, y1 = wgs84(row[0], row[1])
                    origin = row[0], row[1]
                    if target.buffer(x).intersects(Point(x1, y1)):
                        i = i + 1
                        return row[0], row[1]
                        #return  str(i)+' : '+unicode(row[3])+' ('+unicode(row[2])+','+unicode(row[4])+ u') meydanı '+str(distance(origin, target1))+  u' km uzakta'
                        #print str(target.distance(Point(x1,y1)))+   " uzaklikta"
                        #print str(distance(origin, target1))+  '   km uzaklıkta'
                        #print target1, origin
                        rows.remove(row)
                        #break
            if (i == 0):
                print("Yakın havaalanı bulamadım")
        else:
            print("Uygun havaalanı bulamadım")





                        #print u"Size gitmek istediğiniz adrese en yakın "+unicode(row[2])+'('+unicode(row[3])+','+unicode(row[4])+') meydanini onerebilirim.'


'''
                       #if target.buffer(x).intersects(Point(x1, y1)):
                            #print row
                            #print u"Size gitmek istediğiniz adrese en yakın "+unicode(row[2])+'('+unicode(row[3])+','+unicode(row[4])+') meydanini onerebilirim.'
                            #break




         curs = call.cursor()


 curs.execute("SELECT  Lat, Lon FROM destinations WHERE CityName = '%s' "%(i))
            abc = curs.fetchall()
            b = (abc)
            print a
            #for x in range (0,500,50):
                #if a.buffer(50).intersects

#for x in range(0, 500, 1):
    #if p.buffer(x).intersects(a):
       # print str(x)+" de oldu. ve "+str(p.distance(a))+" uzakta"
       # break
#print p.area
#print p.length
#print a.area

'''