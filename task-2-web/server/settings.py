from flask import Flask, request, Response, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bajra.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False