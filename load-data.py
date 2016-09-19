# load-day.py - Python script designed to import data from the demo-data-extract.csv file
# (distributed with this project) into the 'aarhus' table in your instance of Riak TS

from riak import RiakClient
from datetime import datetime
import csv

table_name = "aarhus"
            
client = RiakClient()

totalcount = 0
batchcount = 0
batchsize = 100

ds = []
table = client.table(table_name)

# Open the csv data file
with open('./demo-data-extract.csv', 'rU') as infile:
	#r Load the file into reader 
    reader = csv.reader(infile)
    #Iterate over each line in the file
    for line in reader:
		if line[0] != 'status':
			# Create a row for each line
			new_record = [line[0], str(line[3]), datetime.strptime(line[5],'%Y-%m-%dT%H:%M:%S'), int(line[1]), int(line[2]), int(line[4]), int(line[6])]
			
			# Add the new row to our data set (a list of lists)
			ds.append(new_record)
			batchcount = batchcount + 1
			totalcount = totalcount + 1

			# If the ds size matches the batch size write the batch of rows
			# to Riak TS (optimal size is roughly 100 rows)
			if batchcount == batchsize:
				print "Count at  ", totalcount
				to = table.new(ds)
				to.store()
				batchcount = 0
				ds = []

infile.close()
print "Input file closed"

to = table.new(ds)
if ds:
	to.store()
	
print totalcount