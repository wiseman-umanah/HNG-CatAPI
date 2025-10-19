from flask import Flask, jsonify
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv
from os import getenv 
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# load environment variables
load_dotenv()

# create app
app = Flask(__name__)
CORS(app)

# rate limiting
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/me')
def me():
    # get cat fact
	try:
		response = requests.get('https://catfact.ninja/fact', timeout=5)
		if response.status_code != 200:
			data = {
				"status": "error",
				"message": "Failed to fetch cat fact"
			}
			return jsonify(data), 500
		else:
			fact = response.json().get('fact')

		# create response data
		data = {
			"status": "success",
			"user": {
				"email": "wisemanumanah@gmail.com",
				"name": "Wiseman Umanah",
				"stack": "Python/Flask"
			},
			"timestamp": datetime.now(timezone.utc).isoformat(),
			"fact": fact
		}
		return jsonify(data), 200
	except Exception as e:
		data = {
			"status": "error",
			"message": str(e)
		}
		return jsonify(data), 500



if __name__ == '__main__':
    app.run(port=getenv('PORT', 5000))
