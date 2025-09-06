import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
# Configure Gemini API Key
genai.configure(api_key=api_key)

# Multi-Shot Prompting:
# We give the model MULTIPLE examples to clearly define the style/format we want.

user_prompt = """
Examples:

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

---

Input: Ingredients: pasta, mushrooms, cream
Output:
Recipe Name: Creamy Mushroom Pasta
Ingredients: Pasta, Mushrooms, Cream, Garlic, Olive Oil
Steps:
1. Boil pasta until al dente.
2. Cook mushrooms in olive oil and garlic.
3. Add cream and simmer into sauce.
4. Mix pasta with sauce and serve warm.
Nutrition: High Carbs, Moderate Fat, Medium Protein.

---

Now your turn:
Input: Ingredients: spinach, paneer, tomatoes
Output:
"""

# Use Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate response
response = model.generate_content(user_prompt)

# Print result
print("AI-Generated Multi-Shot Recipe:\n")
print(response.text)
