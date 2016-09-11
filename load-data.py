from riak import RiakClient
from datetime import datetime
import csv
import calendar

table_name = "aarhus"

#
def changetime(stime):
    dt=datetime.strptime(stime,'%Y-%m-%dT%H:%M:%S')
    return calendar.timegm(datetime.timetuple(dt))*1000
            
client = RiakClient()

totalcount = 0
batchcount = 0
batchsize = 100

ds = []
t = client.table(table_name)

with open('./demo-data-extract.csv', 'rU') as infile:
    r = csv.reader(infile)
    for l in r:
		if l[0] != 'status':
			newl = [l[0], str(l[3]) ,datetime.strptime(l[5],'%Y-%m-%dT%H:%M:%S'), int(l[1]), int(l[2]), int(l[4]), int(l[6])]
			totalcount = totalcount + 1

			ds.append(newl)
			batchcount = batchcount + 1

			if batchcount == batchsize:
				#add the records to the table
				print "Count at  ", totalcount
				to = t.new(ds)

				print "Created ts object"
				print "Storage result:  ", to.store()
				batchcount = 0
				ds = []

infile.close()
print "Input file closed"

to = t.new(ds)
if ds:
	print "Storage result:  ",to.store()
	print totalcount