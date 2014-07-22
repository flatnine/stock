#!env/bin/python


import os, csv
import sys
import re

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class Product(Base):
	__tablename__ = 'products'
	prod_id = Column(Integer, primary_key=True)
	style = Column(String(40))
	description = Column( String(100))
	size = Column(String(40))
	ean = Column(String(30), unique=True)

engine = create_engine('sqlite:///stock.db')


Base.metadata.create_all(engine)
