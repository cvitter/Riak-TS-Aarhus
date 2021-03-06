# Riak TS - Aarhus Data Demonstration

This repository contains sample code associated with presentations I gave in San Fransisco, Boston, and NYC for the Basho Scaling Time Series Apps Roadshow (http://basho.com/the-scaling-time-series-apps-roadshow/).

**Note**: The examples here were adapted from work done by Stephen Etheridge (https://github.com/datalemming/rts12-sc-demo) and Sasha Siculars (https://github.com/siculars/riak-ts-aarhus-demo).

To run these examples you will need to have:

- A running instance of Riak TS (https://docs.basho.com/riakts/latest/)
- Python
- The Riak Python client (```pip install riak``` - https://github.com/basho/riak-python-client)
- Jupyter Notebook (http://jupyter.org/)
- Pandas (http://pandas.pydata.org/)
- Matplotlib (```pip install matplotlib```)
- Spark (http://spark.apache.org/downloads.html)
- The Riak Spark Connector (https://github.com/basho/spark-riak-connector)
- Findspark (```pip install findspark```) 

Please see each respective sight for installation information if you don't already have those packages installed.

The data used for these examples is traffic data from Aarhus, Denmark and is part of the Open Data Aarhus project (https://www.odaa.dk/). The demo-data-extract.csv file contains 50,000 traffic observations related to average speed and number of vehicles passing specific exits. 

Once you have all of the packages installed and have downloaded (or cloned) the example code and data, navigate at the command line to the project's directory and launch Jupyter (```>jupyter notebook```). The example code included will:

- Create Aarhus Table.ipynb: Jupyter notebook with Python code that creates the 'aarhus' table
- load-data.py: Python script that imports the demo-data-extract.csv into the 'aarhus' table (```>python load-data.py```)
- Simple Queries.ipynb: Jupyter notebook with Python code that demonstrates the basics of querying the data in the 'aarhus' table
- Pandas Examples.ipynb: Jupyter notebook with Python code that demonstrates the basics of using Pandas to analyze data returned from 'aarhus' table
- Pyspark Examples.ipynb: Jupyter notebook with Python code that demonstrates the basics of using the Riak Spark Connector to connect to and query Riak TS with Spark
