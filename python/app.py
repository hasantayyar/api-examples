# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from bitwala import headers, api
import configparser
import json
import requests
import os

app = Flask(__name__)

def res(data):
	return app.response_class(
			response=data,
			status=200,
			content_type='application/json; charset=utf-8'
		)

@app.route("/")
def main():
	return render_template('homepage.html')

@app.route("/info")
def info():
	return res(api.info())

@app.route("/info/inputs")
def info_inputs():
	return res(api.info_inputs())

@app.route("/info/outputs")
def info_outputs():
	return res(api.info_outputs())

@app.route("/tx/list")
def list_txs():
	page = request.args.get('page') or 0
	return res(api.list_txs(page=page))

@app.route("/tx/create")
def create_tx():
	return res(api.create_tx())

if __name__ == "__main__":
	app.run()
