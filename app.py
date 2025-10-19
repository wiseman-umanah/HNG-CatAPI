from flask import Flask, jsonify
import requests
from datetime import datetime
from dotenv import load_dotenv
from os import getenv 
from flask_cors import CORS

# load environment variables
load_dotenv()

# create app
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/me')
def me():
    # get cat fact
    response = requests.get('https://catfact.ninja/fact')
    fact = response.json().get('fact')

    # create response data
    data = {
        "status": "success",
        "user": {
            "email": "wisemanumanah@gmail.com",
            "name": "Wiseman Umeh",
            "stack": "Python/Flask"
        },
        "timestamp": datetime.now().isoformat(),
        "fact": fact
    }

    # return JSON response with proper headers
    return jsonify(data)



if __name__ == '__main__':
    app.run(port=getenv('PORT', 5000))
