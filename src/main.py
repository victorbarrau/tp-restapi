from datetime import datetime
import json
from random import randint
from unittest import result
from flask import Flask, request,jsonify,Response
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
from random import randint, choices
import datetime as datetime

fake=Faker()


app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://root:root@localhost:5432/store"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False




class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    age = db.Column(db.Integer())
    email = db.Column(db.String(250))
    job = db.Column(db.String(50))
    applications = db.relationship('application')
    
    def __init__(self,firstname,lastname,age,email,job):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email=email
        self.job = job
        
class Application(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    appname= db.Column(db.String(50))
    username=db.Column(db.String(50))
    lastconection = db.Column(db.TIMESTAMP(timezone=True))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    
    
    def __init__(self,appname,username,lastconection):
        self.appname=appname
        self.username=username
        self.lastconection=lastconection
        
        
        
def populate_tables():
    for i in range(1000):
            new_user = User(fake.first_name(),fake.last_name(),randint(20,60), fake.email(), fake.job())
        apps = ["facebook","Twitter","Instagram"]
        nb_app = randint(1,3)
        applications = []
        for app_n in range(0, n_app):
            app = Application(choices(apps),fake.username(),datetime.now()))
            applications.append(app)
        new_user.Application = applications
    
        db.session.add(new_user)
    db.session.commit()
    
    
db=SQLAlchemy(app)
            
@app.route("/user",methods=["POST","GET"]):
def users():
    if request.method == "GET":
        result=User.query.all()
        users=[]
        for row in result:
            user = {
                "id":row.id,
                "firstname":row.firstname,
                "lastname":row.lastname,
                "age":row.age,
                "email":row.email,
                "job":row.job,
            }
            users.append(user)
        return jsonify(users)
def say_hello():
    return "Hello"

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    populate_tables()
    app.run(host="0.0.0.0", port=8080,debug=True)
    