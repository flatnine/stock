#!env/bin/python


import os, csv
import sys
import re

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import Base, Product


style = raw_input("What is the name of the style? ")

filename = style + '.csv'


engine = create_engine('sqlite:///stock.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()



file = os.path.join(os.path.dirname(os.path.abspath(__file__)),filename)

csvfile = open(file,'rb')

reader = csv.reader(csvfile, delimiter=',')

flag = False



for row in reader:
	if re.match(r'^COR',row[0]) and re.match(r'^EAN',row[2]):
		flag = True
		continue
	if re.match(r'^$',row[0]):
		flag = False
	if flag:
		print row
		session.add(Product(style=style.upper(),description=row[0],size=row[1],ean=row[2]))
		session.commit()
