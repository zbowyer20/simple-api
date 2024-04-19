from flask import Flask, jsonify
import os
import logging
import random

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/maybeFails', methods=['GET', 'POST'])
def maybe_fail():
    app.logger.info("Maybe fails called.")
    if random.random() < 0.9:  # random.random() generates a float between 0.0 and 1.0
        return jsonify({"error": "Something went wrong!"}), 500
    else:
        return jsonify({"message": "All is well!"}), 200

@app.route('/api/authenticated')
def authenticate():
    app.logger.info("Authenticate function called")
    return jsonify({"message": "Authenticated successfully."}), 200

@app.route('/api/saml2/authenticate/auth0-saml')
def malicious():
    app.logger.info("Malicious function called")
    return jsonify({"message": "I am malicious!"}), 200

if __name__ == '__main__':
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)

    app.run(debug=True, port=os.getenv("PORT", default=5000))
