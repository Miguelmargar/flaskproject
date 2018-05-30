import os
from flask import Flask, redirect, render_template, request
import json


app = Flask(__name__)

@app.route("/")
def index_page():
    loaded_ads = load_json_ads()
    return render_template("index.html", ads_front=loaded_ads)
    
@app.route("/cars", methods=["POST"]) 
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
    
    ad = {
        "price": price,
        "make": make,
        "model": model,
        "year": year,
        "odometer": odometer,
        "color": color,
        "location": location,
        "email": email,
        "phone": phone
    }
    
    ads_list = load_json_ads()
    
    ads_list.append(ad)
    
    save_json_ads(ads_list)
    
    return redirect("/")


def save_json_ads(ads_list):
    with open("savedads/ads.txt", "w") as outfile:
        json.dump(ads_list, outfile)
        
def load_json_ads():
    if os.path.isfile("savedads/ads.txt"):
        with open("savedads/ads.txt") as json_file:
            return json.load(json_file)
    else:
        return []
        



if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)