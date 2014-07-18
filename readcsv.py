#!env/bin/python


import os, csv
import sys
import re


from sqlalchemy import *
db = create_engine('sqlite:///stock.db')

metadata = BoundMetaData(db)

products = Tables('products', metadata,
	Column('prod_id', Integer, primary_key=True),
	Column('description', String(100)),
	Column('size', String(40)),
	Column('ean', String(30))
)

products.create()

file = '/Users/jonathanb/Downloads/all_tables_combined.csv'

csvfile = open(file,'rb')

reader = csv.reader(csvfile, delimiter=',')

flag = False

insert = products.insert()

for row in reader:
	if re.match(r'^COR',row[0]):
		flag = True
		next
	if re.match(r'^$',row[0]):
		flag = False
	if flag:
		insert.execute(description=row[0],size=row[1],ean=row[2])
