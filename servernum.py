from flask import Flask, request
from flask_restful import Resource, Api, reqparse 

app = Flask(__name__)
api = Api(app)

@app.route('/pi')
def pi():
    num = request.args.get('numsteps')
    numsteps = int(num)
    pi = calcPi(numsteps)
    return str(pi)

def calcPi(steps):
    """ Leibniz formula for arctan(1) = pi/4 """

    sum = 0
    step = 1.0 / steps

    for i in range(steps):
        x = (i + 0.5) * step
        sum += 4.0 / (1.0 + x**2)

    pi = sum * step
    return pi


if __name__ == '__main__':
# added "threades=true" to use multithreading of flask if necessary
    app.run(host="0.0.0.0",port='3000', threaded=True)
