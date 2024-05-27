from flask import Flask, render_template

app = Flask(__name__)

@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    odd_or_even = "odd" if n % 2 != 0 else "even"
    return render_template('odd_or_even.html', n=n, odd_or_even=odd_or_even)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

