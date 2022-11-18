# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 16:50:20 2022

@author: Admin
"""
from flask import Flask,request,render_template
import numpy as np
import pandas as pd 
import pickle
import os
model = pickle.load(open('templates/flight.pkl','rb'))
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("templates/Findstatus.html")
@app.route('/prediction',methods=['POST'])
def predict():
    flight_num = request.form['flight_num']
    month = request.form['month']
    dayofmonth = request.form['dayofmonth']
    dayofweek = request.form['dayofweek']
    origin = request.form['origin']
    if(origin == "msp"):
     origin1,origin2,origin3,origin4,origin5 = 0,0,0,0,1
    if(origin == "dtw"):
     origin1,origin2,origin3,origin4,origin5 = 1,0,0,0,0
    if(origin == "jfk"):
     origin1,origin2,origin3,origin4,origin5 = 0,0,1,0,0
    if(origin == "sea"):
     origin1,origin2,origin3,origin4,origin5 = 0,1,0,0,0
    if(origin == "alt"):
     origin1,origin2,origin3,origin4,origin5 = 0,0,0,1,0
    destination = request.form['destination']
    if(destination == "msp"):
      destination1, destination2, destination3, destination4, destination5 = 0,0,0,0,1
    if(destination == "dkw"):
     destination1, destination2, destination3, destination4, destination5 = 1,0,0,0,0
    if(destination == "jfk"):
     destination1, destination2, destination3, destination4, destination5 = 0,0,1,0,0
    if (destination == "sea") :
     destinationl, destination2, destination3, destination4, destination5 = 0,1,0,0,0 
    if (destination == "alt") :
     destinationl, destination2, destination3, destination4, destination5 = 0,0,0,1,0
    departuretime = request.form['departuretime']
    arrivaltime = request.form['arrivaltime']
    actualdeparturetime = request.form['actualdeparturetime']
    dept15=int (departuretime)-int (actualdeparturetime)
    total = [[flight_num, month, dayofmonth, dayofweek, origin1, origin2, origin3, origin4, origin5, destinationl, destination2, destination3, destination4, destination5]]
    #print (total)
    y_pred = model.predict(total)
    print (y_pred)
    if(y_pred==[0.]):
      ans ="The Flight will be on time"
    else:
      ans ="The Flight will be delayed"
    return render_template("templates/Findstatus.html", showcase = ans)

if __name__=="__main__":
    app.run()