#!/usr/bin/python3
'''
Script to start a flask web application
'''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    '''
    method to display “Hello HBNB!
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    method to display HBNB
    '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    '''
    method to display c/text replacing '_' by ' '
    '''
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    '''
    method to display Python/text with default value
    '''
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    '''
    method to display a number if is an integer
    '''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''
    display a template if n is an integer
    '''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    '''
    display a template if n is an even|odd
    '''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
