import httplib2
import json
from database_setup import insert_value
import psycopg2


def getExchangeData():

    url_usd = "https://api.exchangeratesapi.io/history?start_at=2019-01-01&end_at=2019-10-01&base=USD&symbols=EUR,GBP"
    url_eur = "https://api.exchangeratesapi.io/history?start_at=2019-01-01&end_at=2019-10-01&symbols=USD,GBP"
    url_gbp = "https://api.exchangeratesapi.io/history?start_at=2019-01-01&end_at=2019-10-01&base=GBP&symbols=USD,EUR"
    h = httplib2.Http()

    result_usd = json.loads(h.request(url_usd, 'GET')[1])
    result_eur = json.loads(h.request(url_eur, 'GET')[1])
    result_gbp = json.loads(h.request(url_gbp, 'GET')[1])
    parse_dict(result_eur, result_usd, result_gbp)


def parse_dict(*dict):
    data = ((i[0], some_dict['base'], j, i[1][j]) for some_dict in dict for i in some_dict['rates'].items() for j in i[1].keys())
    for i in data:
        insert_value(""" INSERT INTO RATE (date, source, target, value) VALUES (%s,%s,%s,%s)""",i)



if __name__ == '__main__':
    getExchangeData()
