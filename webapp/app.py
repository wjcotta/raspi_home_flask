from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ClothesWasher')
def ClothesWasher():
	return 'Clothes Washer'

@app.route('/ClothesDryer/')
def ClothesDryer():
	return 'Clothes Dryer'

@app.route('/Dishwasher')
def Dishwasher():
	return 'Dishwasher'


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
