from flask import Flask
import os

app = Flask(__name__)

# Load API key securely from environment variable
API_KEY = os.getenv("API_KEY")

@app.route('/')
def hello():
    if API_KEY:
        return f"Hello! API_KEY loaded from env. Length: {len(API_KEY)}"
    else:
        return "Hello! API_KEY not set. Please configure it as an environment variable."

if __name__ == '__main__':
    app.run(host='192.168.0.0', port=5000)
