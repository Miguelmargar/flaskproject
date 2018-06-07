import os
from flask import Flask, redirect, render_template, request
import json
import random
import string
from pymongo import MongoClient

MONGODB_URI = os.environ.get("MONGODB_URI")
MONGODB_NAME = os.environ.get("MONGODB_NAME")

app = Flask(__name__)

@app.route("/")
def index_page():
    loaded_ads = load_ads()
    return render_template("index.html", ads_front=loaded_ads)
 
@app.route("/create")
def get_create_ad():    
    return render_template("createad.html")
 
   
@app.route("/handle_create", methods=["POST"]) 
def create_ad():

    price       = request.form.get("price")
    make        = request.form.get("make")
    model       = request.form.get("model")
    year        = request.form.get("year")
    odometer    = request.form.get("odometer")
    color       = request.form.get("color")
    location    = request.form.get("location")
    email       = request.form.get("email")
    phone       = request.form.get("phone")
    file        = request.files.get("image")
    
    f = "static/" + os.path.join(os.path.basename("uploads"), file.filename)
    
    main_path = f[:f.find(".")]
    extension = f[f.find("."):]
    random_mix = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    
    if os.path.exists(f):
        f = main_path + "_" + random_mix + extension
    file.save(f)
    
    ad = {
        "price": price,
        "make": make,
        "model": model,
        "year": year,
        "odometer": odometer,
        "color": color,
        "location": location,
        "email": email,
        "phone": phone,
        "image_path": f 
    }
    
    save_to_mongo(ad)
    
    return redirect("/")


def save_to_mongo(ad):
    with MongoClient(MONGODB_URI) as conn:
       db = conn[MONGODB_NAME]
       coll = db["cars"]
       coll.insert(ad)
        
def load_ads():
    with MongoClient(MONGODB_URI) as conn:
        db = conn[MONGODB_NAME]
        coll = db["cars"]
        carad = coll.find()
        car_list = []
        for i in carad:
            car_list.append(i)
        return car_list
            
        

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)