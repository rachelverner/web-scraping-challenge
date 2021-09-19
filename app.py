from flask import Flask, render_template, redirect, request, jsonify
from flask_pymongo import PyMongo
import scrape_mars
import json

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def index():
    mars_data = mongo.db.collection.find_one()
    return render_template("index.html", mars=mars_data)

@app.route("/scrape")
def scrape():

        # Run the scrape function
    mars_info = scrape_mars.scrape_info()

    mongo.db.collection.update({}, mars_info, upsert=True)

    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)