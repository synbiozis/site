#! /usr/bin/python
# -*- coding:utf-8 -*-
 
from flask import Flask
from os import walk
import flask
app = Flask(__name__)

app.secret_key = "test"
 
@app.route('/')
def index():

	return flask.render_template('news.html')
	
@app.route('/videos/')
def clip():
	return flask.render_template('clip.html')

@app.route('/test/')
def test():
	return flask.render_template('test.html')
	
@app.route('/bones/')
def bones():
	flask.flash(u'Vous etes arrivés aux news !', 'success')
	flask.flash(u'Merde, il y a un probleme...', 'error')
	return flask.render_template('bones.html')


@app.context_processor
def toTemplates():
	def newsfile():
		vals = []
		for i, j, k in walk("static/news"):
			#/home/synbiozis/site/static/news/
			for elt in k:
				vals.append(elt)
	
		return vals
		
	def readfile(f):
		with open('static/news/'+str(f), 'r') as f:
			return f.read().split("\n")

	def videos():
		with open('static/videos/videos', 'r') as f:
			return f.read().split("\n")
			
	return dict(news=newsfile(), readfile=readfile, videos=videos())

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
