# -*- coding: utf-8 -*-
import hashlib
import hmac
import urllib
import json

def signature(method, data, url, nonce, secret):
    isGet = method == 'GET'
    content = ""
    if isGet:
        content = bool(data) and str(urllib.parse.urlencode(data)) or ""
    else:
        content = str(json.dumps(data, separators=(',', ':')))
    fullUrl = url
    if isGet and bool(content):
        fullUrl = "%s?%s" % (fullUrl, content)
    bodyHash = hashlib.sha256(content.encode('utf-8')).hexdigest()
    msg = fullUrl + bodyHash + str(nonce)
    s = hmac.new(secret.encode('utf-8'), msg.encode('utf-8'), hashlib.sha512)
    return s.hexdigest()
