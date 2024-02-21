from flask import Flask, jsonify
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

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
