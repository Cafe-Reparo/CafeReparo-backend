from flask import Flask, render_template
from flask_cors import CORS
import json

from src.database.connection import get_connection

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/test')
def test():
    return json.dumps(get_connection())


if __name__ == '__main__':
    app.run()
