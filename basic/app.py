from flask import Flask, request, abort, jsonify, session, render_template
from flask_session import Session
from models import db, User
from config import ApplicationConfig
import hashlib

app = Flask(__name__)
app.config.from_object(ApplicationConfig)


server_session = Session(app)
db.init_app(app)


with app.app_context():
    db.create_all()

@app.route("/", methods=['GET'])
def homepage():
    return "<p>This is the homepage</p>"

@app.route("/register", methods=["GET"])
def register():
    return render_template('./register.html')

@app.route("/submit_register", methods=['POST'])
def register_user():
    email = request.json["email"]
    password = hashlib.sha256(request.json["password"].encode('utf-8')).hexdigest()
    
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


@app.route("/login", methods=["GET"])
def login():
    return render_template('./login.html')

@app.route("/submit", methods=["POST"])
def submit_login():
    email = request.form["email"]
    password = hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest()

    user = User.query.filter_by(email=email).first()
    
    if user == None:
        return jsonify({"error": "Unauthorized"}), 401
    
    if user.password != password:
        return jsonify({"error": "Unauthorized"}), 401
    
    session["user_id"] = user.id

    return jsonify({
        "id": user.id,
        "email": user.email
    })

@app.route("/getname")
def get_name():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Unauthorized"})
    
    user = User.query.filter_by(id=user_id).first()
    
    return jsonify({
        "name": user.email
    })

@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return render_template("./login.html")

if __name__ == "__main__":
    app.run(debug=True)