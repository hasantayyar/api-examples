from bitwala import headers
import requests
import config 

# trust the certificate
# if you want to verify the certificate 
# see http://urllib3.readthedocs.io/en/latest/user-guide.html#ssl
requests.packages.urllib3.disable_warnings()

def get(path, data):
	request_headers = headers.prepare(path=path, data=data)
	r = requests.get("%s%s" % (config.bitwala['api_host'], path), 
		headers=request_headers, 
		timeout=10, verify=False)
	return r.text.encode('utf-8')

def info():
	return get(path="/api/v1/info", data=None)

def info_inputs():
	return get(path="/api/v1/info/inputs", data=None)

def info_outputs():
	return get(path="/api/v1/info/outputs", data=None)