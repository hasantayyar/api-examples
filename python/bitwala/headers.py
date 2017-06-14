import hashlib
import json
from bitwala import signing
import time
import config 

m_seconds = lambda: int(round(time.time() * 1000))

'''
Prepare headers for the Bitwala Rest API
This will generate a dictionary with keys
- x-bitwala-signature
- x-bitwala-nonce
- x-bitwala-token
- Content-Type
'''
def prepare(method, path, data):
    nonce = str(m_seconds())
    headers = {
        'Content-Type': 'application/vnd.api+json',
        'x-bitwala-signature': signing.signature(method=method, 
            data=data, 
            url=path, 
            nonce=nonce, 
            secret=config.bitwala['api_token_secret']), 
        'x-bitwala-nonce': nonce, 
        'x-bitwala-token': config.bitwala['api_token_id']}
    return headers