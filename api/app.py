from flask import Flask, request
from calculator import add, divide, subtract, multiply

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello there"


@app.route("/add")
def calculate_add():
    return {"result": add(request.args["number1"], request.args["number2"])}


@app.route("/divide")
def calculate_divide():
    return {"result": divide(request.args["number1"], request.args["number2"])}


@app.route("/subtract")
def calculate_subtract():
    return {"result": subtract(request.args["number1"], request.args["number2"])}


@app.route("/multiply")
def calculate_multiply():
    return {"result": multiply(request.args["number1"], request.args["number2"])}