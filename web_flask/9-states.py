#!/usr/bin/python3
'''
script that starts a Flask web application
'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.state import City
app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    '''each request you must remove the current SQLAlchemy Session
    '''
    storage.close()


@app.route('/states', defaults={'id': ''}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    '''
    load all cities of a state with its id
    '''
    states = storage.all(State)
    cities = storage.all(City)
    return render_template(
        "9-states.html", states=states, cities=cities, id=id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
