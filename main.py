#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask, request
import MySQLdb as mdb
import flask
app = Flask(__name__)

app.secret_key = "syn"

con = mdb.connect('mysql.server', 'synbiozis', 'synbioz@database', 'synbiozis$default')
cur = con.cursor()

@app.route('/')
def index():
    return flask.render_template("news.html")

@app.route('/videos/')
def clip():
    return flask.render_template('clip.html')

@app.route('/bones/')
def bones():
    flask.flash(u'Vous etes arrivés aux news !', 'success')
    flask.flash(u'Merde, il y a un probleme...', 'error')
    return flask.render_template('bones.html')




@app.route('/news/<name>')
def news(name):
    cur.execute("SELECT title, content FROM News WHERE title='"+name+"'")
    rows = cur.fetchall()
    if rows:
        return flask.render_template_string("""
        <h2>""" + rows[0][0] + """</h2>

        <p>""" + rows[0][1] + """</p>""")
    return "This news doesn't exist."



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


@app.route('/ann/')
def ann():
    return flask.render_template('perceptron.html')
@app.route('/ann/', methods=['GET', 'POST'])
def ann():
    if request.method == 'GET':
        return flask.render_template('perceptron.html')

    if request.form['pass'] == "kabou":

        flask.flash(u'Everything\'s just fine...', 'success')
        return flask.redirect(flask.url_for('ann'))
    else:
        flask.flash(u'Mauvais mot de passe', 'error')
        return flask.redirect(flask.url_for('ann'))

@app.route('/settings/')
def settings():
    return flask.render_template('settings.html')



@app.route('/tests/')
def tests():
    return flask.render_template('tests.html')


@app.context_processor
def temp():
    def removeSpace(val):
        return val.replace(' ', '%20')

    def clips():
        db = mdb.connect('mysql.server', 'synbiozis', 'synbioz@database', 'synbiozis$default')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Clip")

        rows = cursor.fetchall()
        return rows

    def nbrNews():
        db = mdb.connect('mysql.server', 'synbiozis', 'synbioz@database', 'synbiozis$default')
        cursor = db.cursor()
        cursor.execute("SELECT title, content FROM News")

        return len(cursor.fetchall()) -1

    def readnews():
        db = mdb.connect('mysql.server', 'synbiozis', 'synbioz@database', 'synbiozis$default')
        cursor = db.cursor()
        cursor.execute("SELECT title, content FROM News")
        rows = cursor.fetchall()
        return rows



    return dict(removeSpace=removeSpace, clips=clips, nbrNews=nbrNews(), readnews=readnews())



if __name__ == '__main__':
    app.run(debug=False)










