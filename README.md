# Spam Email Detection API

A simple API that detects whether an email is spam or not using machine learning.

## Features

- REST API endpoint for spam detection
- Simple web interface for demonstration
- Detailed API documentation
- Built with Flask and scikit-learn

## Demo

The live demo is available at: [Your deployed URL here]

## Installation

1. Clone this repository
```
git clone https://github.com/yourusername/spam-detection-api.git
cd spam-detection-api
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Run the application
```
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Deploy to Heroku

1. Create a Heroku account if you don't have one
2. Install the Heroku CLI
3. Login to Heroku
```
heroku login
```

4. Create a new Heroku app
```
heroku create your-app-name
```

5. Push to Heroku
```
git push heroku main
```

## API Documentation

### Endpoint: `/predict`

**Method:** POST

**Content-Type:** application/json

**Request Format:**
```json
{
    "email": "Your email content here"
}
```

**Response Format:**
```json
{
    "is_spam": true/false,
    "spam_probability": 0.95,
    "classification": "Spam"/"Not Spam"
}
```

## Project Structure

```
spam-detection-api/
│
├── app.py                  # Main application file
├── models/                 # Directory for model files
│   ├── spam_model.pkl      # Trained spam detection model
│   └── vectorizer.pkl      # Vectorizer for text preprocessing
├── templates/              # HTML templates
│   └── index.html          # Main page with demo
├── requirements.txt        # Python dependencies
├── Procfile               # Heroku deployment file
└── README.md              # This file
```

## How It Works

1. The API receives email content through a POST request
2. The text is preprocessed using the same vectorizer used during training
3. The trained model predicts whether the email is spam or not
4. The API returns the prediction and probability

## Replace the Demo Model

The included model is a simple demonstration. To use your own model:

1. Export your trained model and vectorizer as pickle files
2. Place them in the `models/` directory as `spam_model.pkl` and `vectorizer.pkl`
3. Restart the application

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## About the Author

Deo Prakash - https://github.com/deoprakash