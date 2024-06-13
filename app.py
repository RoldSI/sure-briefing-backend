from flask import Flask
from src.user_routes import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)