from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Kubernetes HPA!"

@app.route('/cpu')
def cpu():
    x = 0
    for i in range(10000000):  # CPU 부하 발생
        x += i
    return f"CPU Intensive Task Done!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))