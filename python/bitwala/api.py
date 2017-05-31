from bitwala import headers
import requests
import config 
import json
import urllib

# trust the certificate
# if you want to verify the certificate 
# see http://urllib3.readthedocs.io/en/latest/user-guide.html#ssl
requests.packages.urllib3.disable_warnings()

def get(path, data=None):
	request_headers = headers.prepare(method='GET', path=path, data=data)
	url = "%s%s" % (config.bitwala['api_host'], bool(data) and ("%s?%s"%(path, urllib.parse.urlencode(data))) or path)
	r = requests.get(url, 
		headers=request_headers, 
		timeout=10, verify=False)
	return r.text.encode('utf-8')

def post(path, data):
	request_headers = headers.prepare(method='POST', path=path, data=data)
	r = requests.post("%s%s" % (config.bitwala['api_host'], path), 
		headers=request_headers, 
		timeout=10, verify=False,
		data=json.dumps(data))
	return r.text.encode('utf-8')

def info():
	return get(path="/api/v1/info")

def info_inputs():
	return get(path="/api/v1/info/inputs")

def info_outputs():
	return get(path="/api/v1/info/outputs")

def create_tx():
	data = { 
		"bankAccount": 
			{
				"recipientType": "INDIVIDUAL",
				"firstName": "Satoshi",
				"lastName": "Nakamoto",
				"currency": "EUR", 
				"iban": "DE89370400440532013000"
			},
		"containcurrency": "EUR",
		"recipientType": "INDIVIDUAL"
		}
	return post(path="/api/v1/transactions", data=data)

def list_txs(page=1):
	page = int(page)
	if(page < 1):
		page = 1
	data = {'page': page}
	return get(path="/api/v1/transactions", data=data)
