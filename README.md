## Exchange Rates:

Use exchangeratesapi.io to get the API of exchange rates from 01.01.2019 till 01.10.2019 and download the data into DB

https://api.exchangeratesapi.io/history?start_at=2019-01-01&end_at=2019-10-01&base=USD&symbols=EUR,GBP

## Steps:
### Create DB:

- Using PostgreSQL and python to create db

### Download the data into DB:

- Call the API URL using http request to get the data in JSON form
- Convert the JSON form to python dictionary and parse the dictionary to get the data from it
- Insert the data into DB

## Run:

- First run `database_setup.py` to create the DB
- run `exchange_data.py` to load the data into DB
- run `data_analysis.py` to run the postgres qurey
