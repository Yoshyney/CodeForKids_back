import sys
import os
sys.path.append(os.environ['WORKSPACE'])

from Flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

app.run(host='0.0.0.0', port=3001)
