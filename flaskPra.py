# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask

app = Flask(__name__) 

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"     
@app.route("/")
def index():
    return "Index page"
@app.route("/user/<username>")
def profile(username):
    return f"{username}'s profile"                                
if __name__=="__main__":
    app.run()
    