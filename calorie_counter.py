from openai import OpenAI
from dotenv import load_dotenv
import base64
import json
import sys

load_dotenv()
client = OpenAI()

def get_calories_and_glucose_from_image(image_path):
    with open(image_path, "rb") as image:
        base64_image = base64.b64encode(image.read()).decode("utf-8")

    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": """You are a dietitian. Analyze the meal image for calories and glucose impact. Use this JSON format:

{
    "reasoning": "reasoning for the calculations",
    "food_items": [
        {
            "name": "food item name",
            "calories": "calories in the food item",
            "glucose_impact": "low/medium/high"
        }
    ],
    "total": "total calories in the meal",
    "glucose_assessment": {
        "impact_level": "low/medium/high",
        "explanation": "explanation of glucose impact",
        "estimated_glucose_rise": "estimated glucose rise in mg/dL"
    }
}"""
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Analyze this meal for calories and glucose impact"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            },
        ],
    )

    response_message = response.choices[0].message
    return json.loads(response_message.content)

if __name__ == "__main__":
    image_path = sys.argv[1]
    result = get_calories_and_glucose_from_image(image_path)
    print(json.dumps(result, indent=4))
