import httplib2
import json

def getExchangeData():

    # url = "https://api.exchangeratesapi.io/history?start_at=2019-01-01&end_at=2019-10-01&base=USD"
    url = "https://api.exchangeratesapi.io/history?start_at=2019-01-01&end_at=2019-10-01&symbols=USD"
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    return result['rates']

print(getExchangeData())
