from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from credentials import MONGO_URI

app = Flask(__name__)
app.config["MONGO_URI"]=MONGO_URI
mongo = PyMongo(app)

db = mongo.db.users

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

if __name__ == "__main__":
    app.run(debug=True)