from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ClothesWasher')
def ClothesWasher():
	return render_template('appliance.html')

@app.route('/ClothesDryer/')
def ClothesDryer():
	return 'Clothes Dryer'

@app.route('/Dishwasher')
def Dishwasher():
	return 'Dishwasher'

@app.route('/hello/<name>')
def hello(name):
		return render_template('page.html', name=name)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8090)
