from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS
from credentials import MONGO_URI

app = Flask(__name__)
app.config["MONGO_URI"]=MONGO_URI
mongo = PyMongo(app)

db = mongo.db.users

@app.route("/users", methods=["POST"])
def createUser():
    data = request.json
    id = db.insert_one(data)
    return jsonify({"msg": f"""User '{data["name"]}' created successfully."""})

@app.route("/users", methods=["GET"])
def getUsers():
    users = [{**user, "_id": str(ObjectId(user["_id"]))} for user in db.find()]
    return jsonify(users)

@app.route("/user/<id>", methods=["GET"])
def getUser():
    return "received"

@app.route("/users/<id>", methods=["GET"])
def deleteUser():
    return "received"

@app.route("/users/<id>", methods=["PUT"])
def updateUser():
    return "received"

if __name__ == "__main__":
    app.run(debug=True)