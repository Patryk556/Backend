from flask import Flask, jsonify, request
from flask_cors import CORS
import os

import random
from datetime import date
from rapidfuzz import fuzz

app = Flask(__name__)
CORS(app)  # allow cross-origin from React frontend

# Sample question list
questions = [
    {
        "question": "What is the largest organ in the human body?",
        "options": ["Liver", "Brain", "Skin", "Heart"],
        "answer": 2
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": 1
    },
    {
        "question": "Who painted the famous artwork 'The Starry Night'?",
        "options": ["Pablo Picasso", "Leonardo da Vinci", "Claude Monet", "Vincent van Gogh"],
        "answer": 3
    }
]

@app.route("/api/getQuestion", methods=["GET"])
def get_question():
    return jsonify(questions)

@app.route("/api/submitAnswer", methods=["POST"])
def submit_answer():
    data = request.get_json()
    print("User submitted:", data)
    return jsonify({"status": "received"})

@app.route("/check_guess", methods=["POST"])
def check_guess():
    data = request.json
    user_guess = data.get("guess", "").strip().lower()
    correct_answer = data.get("result", "").strip().lower()

    # Use fuzzy string matching
    similarity = fuzz.ratio(user_guess, correct_answer)
    
    if(similarity < 85):
        return jsonify({"correct": False})  # Example response
    else:
        return jsonify({"correct": True})  # Example response
    
@app.route("/get_date", methods=['GET'])
def get_daily_song():
    today = date.today()
    mmdd = today.strftime("%m%d")
    #mmdd = "0704"
    mmdd = "0626"
    return jsonify({"date": mmdd})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
