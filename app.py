from flask import Flask, request, redirect, render_template, jsonify
from flask_dataset import Dataset
import jinja2
import random
import os

app = Flask(__name__)
app.debug = True
app.config['DATASET_DATABASE_URI'] = 'sqlite:///%s' % os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')

db = Dataset(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/data")
def data():
    data_items = []
    for date_item in db['data'].all():
        data_items.append(date_item)
    random_item = random.choice(data_items)
    return jsonify({'message': random_item['message'].split(',')})

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
