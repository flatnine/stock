#!env/bin/python

import MySQLdb as mdb
import sys
import json

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

import pysolr


# Custom connection
solr = pysolr.Solr('http://localhost:8983/solr/properties', timeout=10)


Base = automap_base()

engine = create_engine('mysql://rhhdb:tiptoes!@www.rentalholidayhomes.com/rhhdb')

# reflect the tables
Base.prepare(engine, reflect=True)

Properties = Base.classes.properties
Cities = Base.classes.cities
Regions = Base.classes.regions
Countries = Base.classes.countries

session = Session(engine)

docs = []

for city in session.query(Cities):
	print city.title

for property in session.query(Properties):
	docs.append({'id' : property.id, 
			'title': property.title, 
			'description': property.description
			})
	
#for doc in docs:
#print json.dumps(docs)



#solr.add(docs)

#solr.optimize
