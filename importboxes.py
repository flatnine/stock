#!env/bin/python


import os, csv
import sys
import re
import yaml

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Base, Product


count = 1;

filename = 'flipflopscity.yml'


engine = create_engine('sqlite:///stock.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()



file = os.path.join(os.path.dirname(os.path.abspath(__file__)),filename)

yamlfile = open(file,'rb')
boxes = yaml.load(yamlfile)

for box in boxes:
	print "BOX: " + str(count)
	count += 1
	if box['box']:
		for item in box['box']:
			print item