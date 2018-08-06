# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:51:07 2018
@author: audrey roumieux
Projet:
Description:
"""
from __future__ import division, print_function

# Flask utils
from flask import Flask, request, render_template, redirect
from gevent.wsgi import WSGIServer

# Define a flask app
app = Flask(__name__)


@app.route('/voyage')
def formulaire():
    res = "..."
    return render_template('formulaireVoyage.html', data=res)


if __name__ == '__main__':
    app.run(port = 5000, debug = True) 