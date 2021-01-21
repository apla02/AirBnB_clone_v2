#!/usr/bin/python3
'''script that starts a Flask web application
'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    '''After each request you must remove the current SQLAlchemy Session
    '''
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filters_popover():
    '''
    filters and popover
    '''
    s = storage.all(State)
    c = storage.all(City)
    a = storage.all(Amenity)
    return render_template(
        '10-hbnb_filters.html', states=s, cities=c, amenities=a)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
