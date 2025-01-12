from flask import Flask
from fastapi import FastAPI

# app = Flask (__name__)

# @app.route ('/Home')

# def hello_world():

#     return 'Hello, World!'

# app.run(debug=True)

app = FastAPI()
@app.get("/users")

def list_users():

  return [{"username": "Jim"}, {"username": "Pam"}]


# app = FastAPI()
# @app.post("/users")

# def list_users():

#   return [{"username":"Jim"}, {"username":"Pam"}]


# app = FastAPI()
# @app.route("/users",methods = ["GET"])

# def list_users():

#     return [{"username": "Jim"}, {"username": "Pam"}]

# app = FastAPI()
# @app.route("/users",method = ["POST"])

# def list_users():

#   return [{"username": "Jim"}, {"username": "Pam"}]