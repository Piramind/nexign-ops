from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    files = os.listdir('app')
    return '<br>'.join(files)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
