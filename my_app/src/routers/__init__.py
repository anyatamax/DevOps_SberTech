from flask import Flask, jsonify, send_from_directory
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("routers.config.Config")
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, email):
        self.email = email


@app.route("/")
def test_app():
    return "This is test docker app"


@app.route("/users")
def get_all_users():
    result = db.session.query(User.email).all()
    result = [row[0] for row in result]
    return jsonify(users=result)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)