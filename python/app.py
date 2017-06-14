# -*- coding: utf-8 -*-
'''
This module works as a router of the web app.
This is also the entry point of the web app.

'''
from flask import Flask, render_template, request
from bitwala import headers, api
import configparser
import json
import requests
import os

APP = Flask(__name__)

def res(data):
    '''
    response wrapper
    - get the response data as dict object
    - return as response class with json header
    '''
    return APP.response_class(
        response=data,
        status=200,
        content_type='application/json; charset=utf-8'
        )

@APP.route("/")
def main():
    return render_template('homepage.html')

@APP.route("/info")
def info():
    return res(api.info())

@APP.route("/info/inputs")
def info_inputs():
    return res(api.info_inputs())

@APP.route("/info/outputs")
def info_outputs():
    return res(api.info_outputs())

@APP.route("/tx/list")
def list_txs():
    page = request.args.get('page') or 0
    return res(api.list_txs(page=page))

@APP.route("/tx/create")
def create_tx():
    return res(api.create_tx())

if __name__ == "__main__":
    APP.run()
