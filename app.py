from flask import Flask, render_template, redirect, requests
from flask_pymongo import PyMongo
import scrape_mars
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/phone_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_data = mongo.db.collection.find_one()
    print(mars_data)
    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape()
    mongo.db.collection.update({}, mars_data, upsert=True)


if __name__ == "__main__":
    app.run(debug=True)