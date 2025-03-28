# Based on this video: https://www.youtube.com/watch?v=kng-mJJby8g

# Initializes/creates our flask app, must be done anytime you make one
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#imports views from our views file, these are our web pages
from views import views
app.register_blueprint(views, url_prefix="/") #sets the root

# Basic setup to get the app running
# 'debug=True' is nice because it lets the app refresh with new code each time
# you do. No need to re-run the backend code every time there's a new change
if __name__ == '__main__':
    app.run(debug=True, port=8000)
