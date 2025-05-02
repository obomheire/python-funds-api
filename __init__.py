from dotenv import load_dotenv
load_dotenv()
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

# app.config["SQLALCHEMY_DATABASE_URL"] = os.getenv("POSTGRES_DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URL"] = "postgresql://zackoverflow:Secret%40123@localhost:5432/postgres"
db.init_app(app)
