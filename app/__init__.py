from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

import os

app = Flask(__name__)

app.config.from_object('config')

app.secret_key = os.environ.get('SECRET')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

@app.get('/')
def index():
    return "Our app works"

from app.book.endpoints import book
app.register_blueprint(book)
from app.user.endpoints import user
app.register_blueprint(user)