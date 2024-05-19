#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """Displays a list of states and their cities"""
    states = storage.all("State").values()
    states_sorted = sorted(states, key=lambda x: x.name)
    return render_template('9-states.html', states=states_sorted)


@app.route('/states/<id>', strict_slashes=False)
def cities_list(id):
    """Displays a list of cities for a given state"""
    state = storage.get("State", id)
    if state:
        cities_sorted = sorted(state.cities, key=lambda x: x.name)
        return render_template('9-states.html', state=state, cities=cities_sorted)
    else:
        return render_template('9-states.html', not_found=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

