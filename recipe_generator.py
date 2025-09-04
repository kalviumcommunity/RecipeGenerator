import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API Key
genai.configure(api_key=api_key)

# Define the system prompt with RTFC
system_prompt = """
You are an AI-powered Personalized Recipe Generator.
Follow the RTFC (Role, Task, Format, Constraints) framework:

Role: Act as a professional chef and nutrition assistant.
Task: Generate recipes based on given ingredients, dietary preferences, and constraints.
Format: Provide recipe name, ingredients, step-by-step instructions, and nutritional breakdown.
Constraints: Ensure recipes are realistic, avoid unavailable items, respect dietary restrictions, and keep steps clear.
"""

# Example user prompt
user_prompt = """
I have: chicken, tomatoes, onions, garlic.
Dietary Preference: Low-carb, High-protein
Time Available: 30 minutes
Cuisine: Indian
Please generate a recipe with nutrition details and possible alternatives.
"""

# Use the latest Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate response
response = model.generate_content([system_prompt, user_prompt])

# Print result
print("AI-Generated Recipe:\n")
print(response.text)
