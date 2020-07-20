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
def getUser(id):
    user = db.find_one({"_id": ObjectId(id)})
    user["_id"] = str(user["_id"])
    return jsonify(user)

@app.route("/users/<id>", methods=["DELETE"])
def deleteUser(id):
    db.delete_one({"_id": ObjectId(id)})
    return {"message": "User deleted."}

@app.route("/users/<id>", methods=["PUT"])
def updateUser(id):
    db.update_one({"_id": ObjectId(id)}, {"$set": request.json})
    return {"message": "User updated."}

if __name__ == "__main__":
    app.run(debug=True)