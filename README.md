# Riak TS - Aarhus Data Demonstration

This repository contains sample code associated with presentations I gave in San Fransisco, Boston, and NYC for the Basho Scaling Time Series Apps Roadshow (http://basho.com/the-scaling-time-series-apps-roadshow/).

To run these examples you will need to have:

- A running instance of Riak TS (https://docs.basho.com/riakts/latest/)
- Python
- The Riak Python client (https://github.com/basho/riak-python-client)
- Jupyter Notebook (http://jupyter.org/)
- Pandas (http://pandas.pydata.org/). 

Please see each respective sight for installation information if you don't already have those packages installed.

The data used for these examples is traffic data from Aarhus, Denmark and is part of the Open Data Aarhus project (https://www.odaa.dk/). The demo-data-extract.csv file contains 50,000 traffic observations related to average speed and number of vehicles passing specific exits. The example code included will:

- Create Aarhus Table.ipynb: Jupyter notebook with Python code that creates the 'aarhus' table
- load-data.py: Python script that imports the demo-data-extract.csv into the 'aarhus' table (```python load-data.py```)
- Simple Queries.ipynb: Jupyter notebook with Python code that demonstrates the basics of querying the data in the 'aarhus' table
- Pandas Examples.ipynb: Jupyter notebook with Python code that demonstrates the basics of using Pandas to analyze data returned from 'aarhus' table
