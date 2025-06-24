from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use a valid model from your list:
model = genai.GenerativeModel("models/gemini-2.0-flash-001")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_msg = request.args.get('msg')
    try:
        response = model.generate_content(user_msg)
        return response.text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

