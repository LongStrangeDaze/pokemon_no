from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager




app = Flask(__name__)
login = LoginManager()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://orgrvkzm:V-lisb6PJIW-7SMbT8ox2E_iaflMVIKa@heffalump.db.elephantsql.com/orgrvkzm"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Trainers(db.Model):
  __tablename__='trainer'
  id=db.Column(db.Integer,primary_key=True)
  fname=db.Column(db.String(40))
  lname=db.Column(db.String(40))
  email=db.Column(db.String(40))
  
  def __init__(self,fname,lname,email):
    self.fname=fname
    self.lname=lname
    self.email=email


app.config.from_object(Config)


from . import routes

