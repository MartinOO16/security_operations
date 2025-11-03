from flask import Flask
import os

app = Flask(__name__)

# hardcoded secret (teaching point)
API_KEY = "SECRET_API_KEY_12345"

@app.route('/')
def hello():
    return f"Hello. API_KEY={API_KEY} PATH={os.getenv('PATH')}"

if __name__ == '__main__':
    app.run(host='192.168.0.0', port=5000)

