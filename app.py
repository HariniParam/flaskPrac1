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

@app.route("/get/students/<rollno>")
def getInfo(rollno):
    return students[f"{rollno}"]["name"]

@app.route("/post/students/<rollno>/<name>/<className>")
def postInfo(rollno,name,className):
    temp={"name":f"{name}","class":f"{className}"}
    students[f"{rollno}"]=temp  
    return "added"  

@app.route("/put/students/<rollno>/<name>/<className>")
def putInfo(rollno,name,className):
    try:
        students[f"{rollno}"]["name"]=f"{name}"
        students[f"{rollno}"]["class"]=f"{className}"
        return "updated"
    except:
        return "No student exist"
if __name__=="__main__":
    app.run()