# Survey → Gemini prompt generation function

def generate_prompt_from_survey(preferences) -> str:
    return f"""
Here is the profile information of a traveler:

- Companion: {preferences.companion}
- Travel Style: {preferences.style}
- Travel Duration: {preferences.duration}
- Driving: {preferences.driving}
- Budget: {preferences.budget}
- Preferred Climate: {preferences.climate}
- Preferred Continent: {preferences.continent}
- Daily Activity Density: {preferences.density}

Based on this user's preferences, please recommend 2~3 travel cities around the world.
If there are enough suitable cities, recommend all 3.

Please respond strictly in the following JSON format.
Follow the structure exactly — ensure it is valid JSON without missing commas, duplicate keys, or any code block formatting (no ```json).

{{
  "data": [
    {{
      "city": "City name",
      "country": "Country",
      "reason": "Reason for matching the user's preferences",
      "schedule": {{
        "day_1": [
          {{ "time": "10:00-13:00", "activity": "Description of activity" }},
          {{ "time": "14:00-17:00", "activity": "Description of activity" }},
          {{ "time": "18:00-20:00", "activity": "Description of activity" }}
        ],
        "day_2": [ ... ],
        ...
        "day_{preferences.duration}": [...]
      }}
    }}
  ]
}}
"""
