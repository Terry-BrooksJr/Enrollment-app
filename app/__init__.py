from flask import Flask,redirect,url_for,render_template,request
from config import Config
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(Config)


db =  MongoEngine()
db.init_app(app)

from app import routes 

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)