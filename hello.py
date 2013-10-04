#! /usr/bin/python
# -*- coding:utf-8 -*-
 
from flask import *
app = Flask(__name__)
 
@app.route('/')
def accueil():
    return render_template('bones.html')
 
if __name__ == '__main__':
    app.run(debug=True)
