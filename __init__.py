from dotenv import load_dotenv

load_dotenv()
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URL"] = os.getenv("POSTGRES_DATABASE_URL")
db.init_app(app)