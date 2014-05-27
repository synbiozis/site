#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask, request
import MySQLdb as mdb
import flask

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from flask import Markup



app = Flask(__name__)

app.secret_key = "syn"

con = mdb.connect('mysql.server', 'synbiozis', 'synbioz@database', 'synbiozis$default')
cur = con.cursor()

@app.route('/')
def index():
    return flask.render_template("main.html")

@app.route('/ga/')
@app.route('/ga/<int:numPage>')
def ga(numPage=0):
    return flask.render_template("ga-"+str(numPage)+".html")

@app.route('/ann/')
@app.route('/ann/<int:numPage>')
def ann(numPage=0):
    return flask.render_template("ann-"+str(numPage)+".html")

@app.route('/bones/')
def bones():
    flask.flash(u'You are at the root of the project !', 'success')
    flask.flash(u'Fucking error...', 'error')
    return flask.render_template('bones.html')


@app.route('/tests/')
def tests():
    return flask.render_template('tests.html')


@app.context_processor
def temp():
    def removeSpace(val):
        return val.replace(' ', '%20')

    def color(code):
        return Markup(highlight(code, PythonLexer(), HtmlFormatter(full=False, style='default')))

    def pythonFile(file):
        with open('/home/synbiozis/site/static/python/'+file+'.py', 'r') as f:
            code = f.read()
        return Markup(highlight(code, PythonLexer(), HtmlFormatter(full=False, style='default')))

    def textFile(file):
        with open('/home/synbiozis/site/static/python/'+file+'.txt', 'r') as f:
            code = f.read()
        #return Markup(highlight(code, PythonLexer(), HtmlFormatter(full=False, style='default')))
        return Markup(code.replace('\n', '<br />'))

    return dict(removeSpace=removeSpace, color=color, pythonFile=pythonFile, textFile=textFile)


if __name__ == '__main__':
    app.run(debug=False)










