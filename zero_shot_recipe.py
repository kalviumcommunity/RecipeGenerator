import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API Key
genai.configure(api_key=api_key)

# Zero-shot prompting:
# We directly ask the model to generate a recipe without giving it any examples.
user_prompt = """
Generate a healthy vegetarian dinner recipe using spinach, paneer, and tomatoes.
Include ingredients, step-by-step instructions, and nutritional breakdown.
"""

# Use Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate response
response = model.generate_content(user_prompt)

# Print result
print("AI-Generated Zero-Shot Recipe:\n")
print(response.text)
