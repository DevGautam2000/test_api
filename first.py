"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 30/05/21 AT 5:04 PM

    to kill: ps -fA | grep python then kill -9 pid
"""
from flask import Flask

app = Flask(__name__)


# create a route using the decorator function

@app.route('/')
def home():
    users = {
        "Gautam": {
            "password": "134",
            "age": 21
        },
        "Rishabh": {
            "password": "7890",
            "age": 21
        },
    }

    return users


app.run(port=5000)
