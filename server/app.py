#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    result = ''
    for i in range(0, parameter):
        result += f'{i}\n'
    return result

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1,num2,operation):
    if operation == "+":
        return f'{num1 + num2}'
    elif operation == "-":
        return f'{num1 - num2}'
    elif operation == "*":
        return f'{num1 * num2}'
    elif operation == "%":
        return f'{num1 % num2}'
    elif operation == "div":
        return f'{num1 / num2}'
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
