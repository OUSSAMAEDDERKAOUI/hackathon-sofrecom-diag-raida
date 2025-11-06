from flask import Blueprint, request, jsonify, Flask, make_response
from app.services.analysis_service import analyze_data
from dotenv import load_dotenv
from flask_cors import CORS
import os

# Import the Gemini SDK
from google import genai
from google.genai.errors import APIError


app = Flask(__name__)

bp = Blueprint("analysis", __name__, url_prefix="/api/analysis")

@bp.route("/", methods=["POST"])
def analyze():
    
    sent_data = request.get_json()
    result = analyze_data(sent_data)

    if result.get("status") == "failed":
        return jsonify({"error": result.get("error")}), 400

    data = result.get("data")


    
    # 1. Load the API key from the .env file
    load_dotenv()
    API_KEY = os.getenv("GEMINI_API_KEY")

    if not API_KEY:
        raise ValueError("GEMINI_API_KEY not found in environment variables or .env file.")
    
    # 2. Initialize the Gemini Client
    # The Client will automatically pick up the API key from the environment variable.
    try:
        client = genai.Client()
    except Exception as e:
        # A common error here is if the API Key is invalid or rate limited
        print(f"Error initializing Gemini client: {e}")
        client = None # Set to None if initialization fails

    # The model we are using (Gemini 2.5 Flash is great for speed and cost/free tier)
    MODEL_NAME = "gemini-2.5-flash"

    if not client:
        return jsonify({"error": "Gemini Client failed to initialize."}), 500

    # Get the prompt from the form data
    user_prompt = str(data.get("received", ""))

    if not user_prompt:
        return jsonify({"error": "Prompt is required."}), 400
    
    user_prompt = "Analyse these student's answers: " + user_prompt

    try:
        # Call the Gemini API
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=user_prompt
        )

        # Return the AI response as a JSON object
        return jsonify({
            "response": response.text,
            "model": MODEL_NAME
        })

    except APIError as e:
        # Handle specific API errors (like rate limits)
        return jsonify({"error": f"Gemini API Error: {e}"}), 500
    except Exception as e:
        # Handle other general errors
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500



    return jsonify({'d': 'Hello'})






# @app.route("/generate", methods=["POST"])
# def generate_text():
#     """Handles the POST request to call the Gemini API."""
    

if __name__ == "__main__":
    # Runs the Flask server
    app.run(debug=True)