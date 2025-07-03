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
        "question": "Which of the following literary works features the character of Jay Gatsby?",
        "options": ["To Kill a Mockingbird", "The Great Gatsby", "1984", "Pride and Prejudice"],
        "answer": 1
    },
    {
        "question": "In what year did the World Wide Web become publicly available?",
        "options": ["1985", "1991", "1995", "2000"],
        "answer": 1
    },
    {
        "question": "Which ancient civilization is credited with inventing concrete?",
        "options": ["Ancient Egypt", "Ancient Greece", "Ancient Rome", "Mesopotamia"],
        "answer": 2
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
    mmdd = "0626"
    return jsonify({"date": mmdd})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
