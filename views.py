# Instead of having to clutter the app.py file with all of our different web pages
# we can put all of them in one file here as 'blueprints'

# Init/create the Blueprint and call it views
# 'render_template' is the package that helps us view the html files in templates folder
# Request helps us handle queries like .../profile?name=Joe
# Jsonify helps us return our JSON and handle it when it comes in
# Redirect and url_for help redirect users to other pages
from flask import Blueprint, render_template, request, jsonify, redirect, url_for
views = Blueprint(__name__, "views")

# JSON INFORMATON
latest_json = {}
comments = []


# This will take in JSON data and then post it on the /data page
# Use the testFile.py file to see if the site can get a JSON POST request
@views.route("/data", methods=["GET", "POST"])
def get_data():
    global latest_json  # Ensure we can update/get the variable

    if request.method == "POST":
        latest_json = request.get_json()  # Store latest JSON data to our glocal as it comes in
        return jsonify(latest_json)  # Send response back

    # When visiting /data in a browser, display the latest JSON
    return render_template("displayJSON.html", data=latest_json)


@views.route("/inputting", methods=["GET", "POST"])
def inputting():
    global comments

    if request.method == "GET":
        return render_template("inputting.html", comments=comments)

    comments.append(request.form["comment"])
    return redirect(url_for('views.inputting'))


@views.route("/")
def home(): # Remember that def means defining a function, i.e. home
    # Renders our index.html file in the templates folder for the home page
    # You can put as many var.'s in the return as you want, they can be gotten from the webpage from there
    return render_template("index.html")
