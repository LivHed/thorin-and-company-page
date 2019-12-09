import os
import json
from flask import Flask, render_template, request, flash  #import the flask app, and the render_template()function, the request library from Flask, and the flash function.

app = Flask(__name__)  #then create an instance of this and storing it in the variable app. The argument __name__ is a built in python variable.
app.secret_key = 'some_secret'  

@app.route('/')   #the @ sign, the decorator (pie notation), is a way of wrapping functions.
def index():
    return render_template("index.html")
    
@app.route('/about')
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template('about.html', page_title="About", company_data=data)
    
@app.route('/about/<member_name>')
def about_member(member_name):
    member = {}
    
    with open("data/company.json", "r") as json_data:
         data = json.load(json_data)
         for obj in data:
            if obj["url"] == member_name:
                member = obj
                
    return render_template("member.html", member=member)
    
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message".format(
             request.form["name"]
        ))
    return render_template("contact.html", page_title="Contact")
    
@app.route('/careers')
def careers():
    return render_template("careers.html", page_title="Careers")

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            