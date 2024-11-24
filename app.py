from flask import Flask, render_template, g
from flask_cors import CORS
from src.routes.user import user_bp
from src.routes.repair import repair_bp

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

app.register_blueprint(user_bp)
app.register_blueprint(repair_bp)


@app.teardown_appcontext
def close_client(exception):
    client = g.pop("db_client", None)
    if client is not None:
        client.close()


@app.route('/')
@app.route('/home')
@app.route('/api')
@app.route('/api/home')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
