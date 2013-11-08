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

    return d
call = lite.connect("C:/Projects/pgs_geocode.sqlite")

with call:
        cityName = raw_input('Şehir adı gir: ')
        curs = call.cursor()
        curs.execute("SELECT  Lat, Lon, CityName, Airport, Country FROM destinations WHERE CityName like '%s'"%('%'+cityName+'%'))
        rows = curs.fetchall()
        coor = None
        if (len(rows) > 0):
            print u"Verdiğiniz şehirdeki en yakın havaalanları:"
            i = 0
            for row in rows:
                i = i + 1
                print str(i) +' : ' + row[3] +' - ' + row[2] + ' , ' + row[4]
        else:
            url="http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % urllib.quote(cityName)
            response = urllib2.urlopen(url)
            js_response = json.load(response)
            #print len(js_response['results'])
            if (len(js_response['results']) > 1):
                print u"Adres tayini yapmaya çalışıyorum, birden fazla olasılık buldum:"
                i = 0
                coords = []
                for address in js_response['results']:
                    coor = address['geometry']['location']
                    coords.append(coor)
                    i = i + 1
                    print str(i) + ' : ' + address['formatted_address']
                secilen_adres = raw_input(u'Listeden bir adres seçin :')
                while (int(secilen_adres) > len(js_response['results']) or int(secilen_adres) < 0):
                    secilen_adres = raw_input(u'Listeden bir adres seçin :')
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
                rows = curs.fetchall()
                for row in rows:
                    x1, y1 = wgs84(row[0], row[1])
                    origin = row[0], row[1]
                    #print origin


                   # print x1, y1

                    for x in drange(0,0.035,0.001):
                        l = 0
                        if target.buffer(x).intersects(Point(x1, y1)):
                            '''secenekler = []
                            l = 0
                            a = [row[2], row[3], row[4]]
                            for b in a :5
                                secenekler.append(a)
                                l= l+1
                                print str(l) +' : '+ a[0] '''






                            print  u"Size gitmek istediğiniz adrese en yakın " +  str(distance(origin, target1))+  '  km uzakliktaki ' + unicode(row[2])+'('+unicode(row[3])+','+unicode(row[4])+ ') meydanini onerebilirim.'

                            print str(target.distance(Point(x1,y1)))+   " uzaklikta"

                            #print str(distance(origin, target1))+  '   km uzaklıkta'
                            print target1, origin

                            break

                else:
                    print("uygun havaalanı bulamadım")


            else:
                print("uygun havaalanı bulamadım")





                        #print u"Size gitmek istediğiniz adrese en yakın "+unicode(row[2])+'('+unicode(row[3])+','+unicode(row[4])+') meydanini onerebilirim.'