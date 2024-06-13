from flask import Flask
from flask_cors import CORS
from src.user_routes import user_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(user_bp)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)