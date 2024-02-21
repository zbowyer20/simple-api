from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/api/authenticated')
def authenticate():
    return jsonify({"message": "Authenticated successfully."}), 200

@app.route('/api/saml2/authenticate/auth0-saml')
def malicious():
    return jsonify({"message": "I am malicious!"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
