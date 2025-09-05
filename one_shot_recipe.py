import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API Key
genai.configure(api_key=api_key)

# One-Shot Prompting:
# We give the model ONE example of what we want, then ask it to do something similar.

user_prompt = """
Example:
Input: Ingredients: chicken, rice, onions
Output:
Recipe Name: Spicy Chicken Rice
Ingredients: Chicken, Rice, Onions, Spices
Steps:
1. Cook rice until fluffy.
2. Sauté onions and spices.
3. Add chicken and cook until tender.
4. Mix with rice and serve hot.
Nutrition: High Protein, Moderate Carbs, Low Fat.

Now your turn:
Input: Ingredients: spinach, paneer, tomatoes
Output:
"""

# Use Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate response
response = model.generate_content(user_prompt)

# Print result
print("AI-Generated One-Shot Recipe:\n")
print(response.text)
