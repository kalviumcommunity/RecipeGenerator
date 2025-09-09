import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API Key
# Recommended: set GEMINI_API_KEY in your environment, do NOT hardcode the key in source.
API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")
genai.configure(api_key=API_KEY)

# System prompt using RTFC (Role, Task, Format, Constraints)
system_prompt = """
You are a helpful, safety-aware AI assistant: a professional chef and nutrition advisor.
Follow RTFC:
- Role: Professional chef + nutrition assistant.
- Task: Generate a realistic recipe tailored to the user's ingredients and constraints.
- Format: First provide a VERY BRIEF numbered reasoning summary (max 3 short items) — a high-level justification for the choices made (e.g., why a particular cooking method or spice was chosen). Then output the final recipe as JSON with keys: recipe_name, ingredients (list), steps (list), nutrition (brief summary), substitutes (list).
- Constraints: Do NOT reveal internal chain-of-thought or long, introspective reasoning. The brief reasoning must be a concise, high-level justification only. Ensure dietary restrictions are respected and steps are realistic for the stated time.
"""

# Example user inputs (these could come from a web form in your app)
ingredients = ["spinach", "paneer", "tomatoes"]
diet = "Vegetarian, High Protein"
time_limit = "25 minutes"
cuisine = "Indian"

# Build the dynamic user prompt
user_prompt = f"""
User Request:
Ingredients: {', '.join(ingredients)}
Dietary Preference: {diet}
Time Available: {time_limit}
Cuisine: {cuisine}

Instructions to the model:
- Provide a VERY BRIEF numbered reasoning summary (max 3 short items) that explains key decisions (e.g., why a quick sauté and paneer pairing works) without exposing internal chain-of-thought.
- Then return the final recipe in JSON following this example schema:

{{
  "recipe_name": "...",
  "ingredients": ["..."],
  "steps": ["..."],
  "nutrition": "approx calories / protein / carbs / fat",
  "substitutes": ["..."]
}}

Now generate the output.
"""

# Choose the Gemini model available in your environment
model = genai.GenerativeModel("gemini-1.5-flash")

try:
    # Send both system and user prompts together for better instruction following
    response = model.generate_content([system_prompt, user_prompt])

    # Print model output (the output should be a short reasoning summary + JSON recipe)
    print(response.text)

except Exception as e:
    print("Error while calling Gemini API:", str(e))
    print("Checklist:")
    print(" - Make sure you installed the SDK: pip install --upgrade google-generativeai")
    print(" - Ensure GEMINI_API_KEY is set in environment or replace the placeholder (avoid committing keys)")
    print(" - Confirm the model name 'gemini-1.5-pro-latest' is available for your account")
