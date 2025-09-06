import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API Key
genai.configure(api_key=api_key)

# Dynamic Prompting:
# The prompt is not static — it is built dynamically from user inputs.

# Example user input (this could come from a form or API request in your app)
ingredients = ["spinach", "paneer", "tomatoes"]
diet = "Vegetarian, High Protein"
time_limit = "20 minutes"
cuisine = "Indian"

# Build dynamic prompt
user_prompt = f"""
Generate a recipe using the following details:

Ingredients: {", ".join(ingredients)}
Dietary Preference: {diet}
Time Available: {time_limit}
Cuisine: {cuisine}

Include:
- Recipe Name
- Ingredients
- Step-by-step Instructions
- Nutritional Breakdown
- Possible Substitutes
"""

# Use Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate response
response = model.generate_content(user_prompt)

# Print result
print("AI-Generated Dynamic Prompted Recipe:\n")
print(response.text)
