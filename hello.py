from flask import Flask

app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def anything():
#     # this func will automatically execute
#     return "<h1> Hello there.!! </h1>"



@app.route('/')
def hello_world():
    # this func will automatically execute
    return "<h1> Hello there.!! </h1>"

@app.route('/ping', methods=['GET'])
def ping():
    return {"message": "Why are you pining me?"}

# @app.route('/ping')
# def ping():
#     return {"message": "Why are you pining me?"}

