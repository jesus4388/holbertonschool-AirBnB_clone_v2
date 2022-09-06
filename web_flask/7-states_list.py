#!/usr/bin/python3
""" Start a Flask web aplication"""

from flask import Flask, render_template
from models import storage
from models.state import State
import os


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list', strict_slashes=False)
def list_state():
    """definition of funtion"""
    if (os.getenv('HBNB_TYPE_STORAGE') == 'db'):
        states = storage.all(State)
        states_list = []
        for key, state in states.items():
            states_list.append(state)
        states_list.sort(key=lambda x: x.name)
        return render_template("7-states_list.html", states=states_list)

@app.teardown_appcontext
def remove(exception=None):
    """remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
