# Import flask and template operators
from flask import Flask, render_template, flash

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Import Flask-Migrate for db migrations
from flask_migrate import Migrate

# Import Flask-Bootstrap for wtf and utils libraries
from flask_bootstrap import Bootstrap

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Define db migrations object
migrate = Migrate(app, db)

# Initiate Flask-Bootstrap ...
Bootstrap(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
  return render_template('404.html'), 404

# Import modules / components using their blueprint handler
from app.mod_auth.controllers import mod_auth as auth_module
from app.main.controllers import main as main_module
from app.mod_catalog.controllers import mod_catalog as catalog_module

# Register blueprint(s)
app.register_blueprint(auth_module)
app.register_blueprint(main_module)
app.register_blueprint(catalog_module)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()