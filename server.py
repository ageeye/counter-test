from flask import Flask, jsonify, request
from random import uniform
app = Flask(__name__)

minmax = range(1, 5)

cars = [ { 'id': id, 'counter': 0. } for id in minmax]
msg_error = {'error': 'ID is out of range! '}


@app.route('/cars/<id>')
def get_car(id):
	if int(id) in minmax:
		pt = int(id)-1
		cars[pt]['counter'] += uniform(0., 100.)
		return jsonify(cars[pt])
	else:
		msg = msg_error
		msg['error'] += str(minmax)
		return jsonify(msg_error)

if __name__ == "__main__":
    app.run((host='0.0.0.0', port=8080, debug=False)

