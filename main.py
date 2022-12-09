from flask import Flask
import time
import random

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello_world():
    time.sleep(random.random())
    return '', 204