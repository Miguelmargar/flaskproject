import os
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

ads = {}

@app.route("/")
def index_page():
    return render_template("index.html")
    
  
def create_ad(methods=["GET"]):
    
    make = request.form.get("make")
    model = request.form.get("model")
    year = request.form.get("year")
    odometer = request.form.get("odometer")
    color = request.form.get("color")
    location = request.form.get("location")
    email = request.form.get("email")
    phone = request.form.get("phone")
    
    ad = {
        "make": make,
        "model": model,
        "year": year,
        "odometer": odometer,
        "color": color,
        "location": location,
        "email": email,
        "phone": phone
    }
    
    ads.update(ad)

def save_ads():
 f = open("ad.txt", "w")
 f.write(ads)
 f.close()
 
 
















if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))