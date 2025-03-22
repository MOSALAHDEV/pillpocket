#!/usr/bin/python3
""" Home Route """
from flask import Flask, render_template


app = Flask(__name__)
@app.route('/', strict_slashes=False)
def home_route():
    """ Home Route """
    return render_template('index.html')

@app.route('/about', strict_slashes=False)
def about_route():
    """ About Route """
    return render_template('about.html')

@app.route('/medications', strict_slashes=False)
def medications_route():
    """ Medications Route """
    return render_template('medications.html')

@app.route('/order', strict_slashes=False)
def order_route():
    """ Order Route """
    return render_template('order.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)