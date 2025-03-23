# Instead of having to clutter the app.py file with all of our different web pages
# we can put all of them in one file here as 'blueprints'

# Init/create the Blueprint and call it views
# 'render_template' is the package that helps us view the html files in templates folder
# Request helps us handle queries like .../profile?name=Joe
# Jsonify helps us return our JSON and handle it when it comes in
# Redirect and url_for help redirect users to other pages
from flask import Blueprint, render_template, request, jsonify, redirect, url_for
views = Blueprint(__name__, "views")


@views.route("/")
def home(): # Remember that def means defining a function, i.e. home
    # Renders our index.html file in the templates folder for the home page
    # You can put as many var.'s in the return as you want, they can be gotten from the webpage from there
    return render_template("index.html", name="Timothy", age=21)


# This is a dynamic page <argument>, changes as the url argument changes
# If you put a name in the URL, index.html will change to match, if not it defaults to above
@views.route("/profile/<username>") #i.e. 127.0.0.1:8000/profile/Johnny
def profile(username):
    return render_template("index.html", name=username)


# Similar to above but uses it as a query from the URL
# Also, the page is 'profile.html' which is an inherited page from 'index.html'
# It's exactly the same page but has different content in it
@views.route("/users") #i.e. 127.0.0.1:8000/users?name=Joe
def users():
    args = request.args
    name = args.get('name')
    return render_template("profile.html", name=name)


# Return JSON instead of HTML to the webpage
@views.route("/json")
def get_json():
    return jsonify({'name' : 'Ashton', 'age' : 21})


# Someone is sending the website data in JSON format
# Then we're going to handle said data
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data) # Whatever we send it, it'll just show on the webpage


# Redirect to a diff page
@views.route("/go-to-home")
def go_to_home():
    # If someone tries going to .../go-to-home it'll send them to .../ our home page
    return redirect(url_for("views.home"))
