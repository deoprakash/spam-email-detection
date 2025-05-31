from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://spam-email-detection-o748.onrender.com"])

# Define file paths
MODEL_PATH = 'models/spam_model.pkl'
VECTORIZER_PATH = 'models/vectorizer.pkl'

# Load the vectorizer
with open(VECTORIZER_PATH, 'rb') as f:
    vectorizer = pickle.load(f)

# Load the trained model
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get email content from request
    data = request.json
    email_content = data.get('email', '')
    
    if not email_content:
        return jsonify({'error': 'No email content provided'}), 400
    
    # Vectorize the email content
    email_vectorized = vectorizer.transform([email_content])
    
    # Make prediction
    prediction = model.predict(email_vectorized)[0]
    spam_probability = float(model.predict_proba(email_vectorized)[0][1])
    
    # Return result
    result = {
        'is_spam': bool(prediction),
        'spam_probability': spam_probability,
        'classification': 'Spam' if prediction == 1 else 'Not Spam'
    }
    
    return jsonify(result)

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
