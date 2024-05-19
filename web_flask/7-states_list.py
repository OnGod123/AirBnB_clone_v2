from flask import Flask, render_template
from models import storage  

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Fetch all State objects from the storage engine (FileStorage or DBStorage)"""
    states = storage.all("State").values()
    
    """Pass the list of State objects to the template for rendering"""
    return render_template('7-states_list.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

