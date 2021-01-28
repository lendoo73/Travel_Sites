from os import environ # this line should go at the top of your file
from flask import Flask
# ------- Setup the database -------
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "my_secret_key"
"""
When we added PostgreSQL to our heroku project, it automatically created that DATABASE_URL environment variable for us. So when our code is run on Heroku, os.environ['DATABASE_URL'] should automatically point to the PostgreSQL database.
"""
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("DATABASE_URL") or 'sqlite:///my_database.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ------- Managing logged in state -------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  # The name of the view to redirect to when the user needs to log in. 


import routes, models

# Initializing the database
#db.create_all()