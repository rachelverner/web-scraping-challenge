from flask import Flask, render_template, redirect, request, jsonify, Markup
from flask_pymongo import PyMongo
import scrape_mars
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd
import json

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

@app.route("/")
def index():
    mars_1 = list(mongo.db.collection.find())
    print(mars_1)
    return render_template("index.html", mars_data=mars_1)
    
@app.route("/scrape")
def scrape():
    mars_dict = scrape_mars.scrape_info()
    #with open('troubleshooting_app.json', 'w') as json_file:
        #json.dump(mars_dict, json_file)
    mongo.db.collection.update({}, mars_dict, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)