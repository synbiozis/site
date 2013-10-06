#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
from os import walk
import MySQLdb as mdb
import flask
app = Flask(__name__)


app.debug = True
app.secret_key = "test"

@app.route('/')
def index():

    return flask.render_template('news.html')

@app.route('/videos/')
def clip():
    return flask.render_template('clip.html')


@app.route('/news/<name>')
def news(name):
    return flask.render_template(name+'.html')


@app.route('/bones/')
def bones():
    flask.flash(u'Vous etes arrivés aux news !', 'success')
    flask.flash(u'Merde, il y a un probleme...', 'error')
    return flask.render_template('bones.html')

@app.route('/test/')
def test():
    return flask.render_template('test.html')


@app.context_processor
def toTemplates():
    def newsfile():
        vals = []
        for i, j, k in walk("/home/synbiozis/site/static/news/"):
            #/home/synbiozis/site/static/news/
            for elt in k:
                vals.append(elt)

        return vals


    def clips():
        con = mdb.connect('mysql.server', 'synbiozis', 'synbioz@database', 'synbiozis$default')
        with con:

            cur = con.cursor()
            cur.execute("SELECT * FROM Clip")

            rows = cur.fetchall()
        return rows


    def readnews(name):
        i = flask.render_template(name+'.html')
        return i.title()


    def readfile(f):
        with open('/home/synbiozis/site/static/news/'+str(f), 'r') as f:
            return f.read().split("\n")

    def videos():
        with open('/home/synbiozis/site/static/videos/videos', 'r') as f:
            return f.read().split("\n")

    return dict(news=newsfile(), readfile=readfile, videos=videos(), readnews=readnews, clips=clips())

if __name__ == '__main__':
    app.run(debug=True)










