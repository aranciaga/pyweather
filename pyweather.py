#!/usr/bin/python2
# coding: utf-8
# pyweather notifier by Rainbow (wlan0)

import urllib2, os

from xml.dom.minidom import parseString
from BeautifulSoup import BeautifulSoup
from lxml import etree

# Choose your Yahoo WOEID Here
# http://woeid.rosselliot.co.nz/lookup/

woeid = "466863"

get = urllib2.urlopen('http://weather.yahooapis.com/forecastrss?w='+woeid+'&u=c')
data = get.read()
get.close()

dom = parseString(data)

#Temperatura
temp = dom.getElementsByTagName('yweather:wind')[0]
tempatr = temp.getAttributeNode('chill')

#Imagen
img = dom.getElementsByTagName('description')[1].toxml()
f = etree.fromstring(img)

for s in f.xpath("//description"):
	page = BeautifulSoup(s.text)
	img = page.find('img')['src']
	temp = tempatr.nodeValue
	os.system('wget '+img+' -O /tmp/weather.jpg > /dev/null 2>&1')
	os.system('notify-send -i /tmp/weather.jpg "Temperatura: '+temp+'*C"')
