#!usr/bin/python3
'''
    Script to initialize a flask web application
'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    '''
        method to return Hello HBNB!
    '''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
