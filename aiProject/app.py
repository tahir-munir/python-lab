from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

model = joblib.load('bbc_news_model.joblib')

# Flask API endpoint - Allow POST requests
@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['text']])
    return jsonify({'category': prediction[0]})

# Flask error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
