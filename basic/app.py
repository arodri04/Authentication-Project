from flask import Flask, request, abort, jsonify, session
from flask_session import Session
from models import db, User
from config import ApplicationConfig

app = Flask(__name__)
app.config.from_object(ApplicationConfig)


server_session = Session(app)
db.init_app(app)


with app.app_context():
    db.create_all()

@app.route("/", methods=['GET'])
def homepage():
    return "<p>This is the homepage</p>"

@app.route("/register", methods=['POST'])
def register_user():
    email = request.json["email"]
    password = request.json["password"]

    user_exists = User.query.filter_by(email=email).first() is not None

    if user_exists:
        return jsonify({"error": "User already exists"}), 409
    

    new_user = User(email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "id": new_user.id,
        "email": new_user.email
    })



if __name__ == "__main__":
    app.run(debug=True)