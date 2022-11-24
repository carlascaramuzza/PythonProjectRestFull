from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Response, request
from config import DevelopmentConfig as dbConfig
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = dbConfig.SECRET_KEY
app.config['DEBUG'] = dbConfig.DEBUG
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + dbConfig.MYSQL_USER + ':' + dbConfig.MYSQL_PASSWORD + '@' + dbConfig.MYSQL_HOST + '/' + dbConfig.MYSQL_DB

