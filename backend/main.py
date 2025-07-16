from flask import Flask, request, jsonify
from flask_cors import CORS
import openai, os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from a .env file

openai.api_key = os.getenv("OPENAI_API_KEY") # Get the OpenAI API key from environment variable

app = Flask(__name__) # Create a Flask app instance
CORS(app) # Enable CORS so frontend from different domain/port can access this backend

@app.route("/ask", methods=["POST"]) # Define a POST route '/ask' where the frontend will send a question

def ask():
    data = request.get_json() # Get JSON data sent in the POST request
    question = data.get("question", "") # Extract the 'question' field from the JSON
    if not question:
        # If no question was provided, return an error message and status code 400
        return jsonify({"error" : "No question provided"}), 400
    
    # Call OpenAI's API with a prompt using chat completion
    response = openai.ChatCompletion.create(
        model="GPT-MODEL-HERE"
        messages=[
            {"role" : "system", "content" : "You are a helpful immigration legal assistant who explains things in simple terms."},
            {"role" : "user", "content" : question}
        ]
    )

    answer = response.choices[0].message.content # Extract the assistant's reply from the response
    return jsonify({"answer" : answer})  # Return answer in JSON format

# Run the app if this file is executed directly
if __name__ == "__main__": 
    app.run(debug=True) # Start the Flask development server with debug mode on