import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# List all available models
models = genai.list_models()

print("Available models:")
for model in models:
    print(model.name)
