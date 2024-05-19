from flask import render_template
from web_flask import app

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB'"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display 'C ' followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Display 'Python ' followed by the value of the text variable"""
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display 'n is a number' only if n is an integer"""
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display an HTML page only if n is an integer"""
    return render_template('number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display an HTML page only if n is an integer"""
    odd_or_even = 'even' if n % 2 == 0 else 'odd'
    return render_template('odd_or_even.html', n=n, odd_or_even=odd_or_even)

