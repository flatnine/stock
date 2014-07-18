#!env/bin/python

import sys
import pprint 
import urllib2
from bs4 import BeautifulSoup

url = 'http://barcode.havaianas.com.br'

response = urllib2.urlopen(url + '/2012.htm')

soup = BeautifulSoup(response)


options = soup.findAll("option")


#print options[1]['value']

for option in options:
	if option.get('value'):
		print url + "/" + option.get('value').encode('utf-8') + " " + option.text.encode('utf-8')