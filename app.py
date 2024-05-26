from flask import Flask
from dotenv import load_dotenv
import os
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
load_dotenv()
CORS(app)
# Get the environment variables
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
