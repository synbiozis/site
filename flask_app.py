#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, request
import MySQLdb as mdb
import flask
app = Flask(__name__)

app.secret_key = "test"

con = mdb.connect('mysql.server', 'synbiozis', 'synbioz@database', 'synbiozis$default')
cur = con.cursor()


@app.route('/')
def index():

    return flask.render_template("news.html")

@app.route('/videos/')
def clip():
    return flask.render_template('clip.html')


@app.route('/news/<name>')
def news(name):
    cur.execute("SELECT title, content FROM News WHERE title='"+name+"'")
    rows = cur.fetchall()
    if rows:
        return flask.render_template_string("""
            {% extends "bones.html" %}

            {% block title %}News{% endblock %}

            {% block section %}

            <h2>""" + rows[0][0] + """</h2>

        	<p>""" + rows[0][1] + """</p>


            {% endblock %}""")
    return "This news doesn't exist."


@app.route('/upload/clip/', methods=['GET', 'POST'])
def uploadClip():
    if request.method == 'GET':
        return flask.render_template('upload.html')

    if request.form['pass'] == "kabou":

        cur.execute("INSERT INTO Clip VALUES(NULL, '" + request.form['title'] + "', '" + request.form['address'] + "', '" + request.form['comment']+"')")

        con.commit()

        return flask.redirect(flask.url_for('clip'))
    else:
        flask.flash(u'Mauvais mot de passe', 'error')
        return flask.render_template('upload.html')



@app.route('/upload/news/', methods=['GET', 'POST'])
def uploadNews():
    if request.method == 'GET':
        return flask.render_template('uploadNews.html')

    if request.form['pass'] == "kabou":
        cur.execute("INSERT INTO News VALUES(NULL, '" + request.form['title'] + "', '" + request.form['content'] + "')")

        con.commit()

        return flask.redirect(flask.url_for('index'))
    else:
        flask.flash(u'Mauvais mot de passe', 'error')
        return flask.render_template('uploadNews.html')


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

    def clips():
        cur.execute("SELECT * FROM Clip")

        rows = cur.fetchall()
        return rows


    def readnews():
        cur.execute("SELECT title, content FROM News")
        rows = cur.fetchall()
        return rows

    def nbrNews():
        cur.execute("SELECT title, content FROM News")
        return len(cur.fetchall()) -1

    def removeSpace(val):
        return val.replace(' ', '%20')

    return dict(readnews=readnews(), clips=clips(), nbrNews=nbrNews(), removeSpace = removeSpace)

if __name__ == '__main__':
    app.run(debug=True)










