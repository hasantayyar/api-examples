# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify
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

if __name__ == "__main__":
	app.run()
