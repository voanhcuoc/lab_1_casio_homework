from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def ui():
    return render_template('index.html')

@app.route('/sin', methods=['POST'])
def sin():
    x = request.json['x']
    return { "result": math.sin(x) }

@app.route('/cos', methods=['POST'])
def cos():
    x = request.json['x']
    return { "result": math.cos(x) }

@app.route('/tan', methods=['POST'])
def tan():
    x = request.json['x']
    return { "result": math.tan(x) }

@app.route('/sqrt', methods=['POST'])
def sqrt():
    x = request.json['x']
    return { "result": math.sqrt(x) }

@app.route('/pow', methods=['POST'])
def pow():
    x = request.json['x']
    y = request.json['y']
    return { "result": math.pow(x,y) }

@app.route('/natural_log', methods=['POST'])
def natural_log():
    x = request.json['x']
    return { "result": math.log(x) }

@app.route('/logarithm_log', methods=['POST'])
def logarithm_log():
    x = request.json['x']
    y = request.json['y']
    return { "result": math.log(x,y) }

@app.route('/fact', methods=['POST'])
def fact():
    x = request.json['x']
    return { "result": math.factorial(x) }

@app.route('/exp', methods=['POST'])
def exp():
    x = request.json['x']
    return { "result": math.exp(x) }

@app.route('/radian', methods=['POST'])
def rad():
    x = request.json['x']
    return { "result": math.radians(x) }

@app.route('/degree', methods=['POST'])
def deg():
    x = request.json['x']
    return { "result": math.degrees(x) }

@app.route('/complex_num', methods=['POST'])
def complex():
    x0 = request.json['x0']
    x1 = request.json['x1']
    r = math.hypot(x0,x1)
    theta = math.atan2(x1,x0)
    result = [r, theta]
    return { "result": result }
    

app.run(port=5000)



