import os
import random
from flask import Flask
import datetime
import time


app = Flask(__name__)


@app.route('/')
def home():
    return 'hi'

@app.route('/fruits')
def fruit():
    return ['tomaTo', 'stRawBerry', 'WaterMelon', 'ApPLE', 'ORanGE', 'beet', 'kIWI']

@app.route('/logs/<int:seconds>')
def create_logs(seconds):
    logs = []
    for i in range(seconds):
        logs.append(f"S{i}:{datetime.datetime.now()},{random.randrange(0,100000)/ 100},{random.randrange(0,100000)/ 100}")
        time.sleep(1)
        
    return logs

if __name__ == '__main__':
    app.run(debug=False, port=5000)