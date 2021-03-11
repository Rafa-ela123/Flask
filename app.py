from flask import Flask, render_template
from flask import *
import os
import random
import pandas as pd
from waitress import serve
app = Flask(__name__)
#app.run(debug = True)

from functions import logins #from logins.py to app.py

"""
cd Desktop/Flask
python app.py
"""

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/grass")
def grass():
    return render_template("grass.html")

@app.route("/<path:dummy>") #always at the end
def others(dummy): #add "dummy" to ()
    return render_template("others.html")

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    #app.run()
    serve(app, host='0.0.0.0', port=8080)
#from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)
    #app.run(debug=True)
