#! /usr/bin/python
# -*- coding:utf-8 -*-
 
from flask import Flask
from os import walk
import flask
app = Flask(__name__)
 
@app.route('/')
def index():
    return flask.render_template('bones.html')
 
@app.route('/news/')
def news():
	return flask.render_template('news.html')

@app.context_processor
def toTemplates():
	def newsfile():
		vals = []
		for i, j, k in walk("static/news"):
			for elt in k:
				vals.append(elt)
	
		return vals
		
	def readfile(f):
		with open('static/news/'+str(f), 'r') as f:
			return f.read().split("\n")
			
	return dict(news=newsfile(), readfile=readfile)

if __name__ == '__main__':
    app.run(debug=True)
