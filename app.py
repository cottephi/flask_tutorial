from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Should read it from os.environ, but osef for now
app.config["SECRET_KEY"] = "somekey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

from routes import *


if __name__ == "__main__":
    app.run(debug=True)
