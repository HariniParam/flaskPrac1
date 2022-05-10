# -*- coding: utf-8 -*-
"""
Created on Tue May 10 17:32:11 2022

@author: 21pt05
"""

students={'21PT05':{"name":"Harini","class":'21PT'},'21PT10':{"name":"abc","class":'21PT'}}
from flask import Flask

app = Flask(__name__) 
@app.route("/get/students")
def getStudents():
    return students


@app.route("/get/students/<id>")
def getInfo(id):
    return students[f"{id}"]["name"]                         
if __name__=="__main__":
    app.run()