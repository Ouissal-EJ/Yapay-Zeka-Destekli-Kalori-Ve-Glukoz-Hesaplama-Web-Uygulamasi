from openai import OpenAI
from dotenv import load_dotenv
import base64
import json
import sys

load_dotenv()
client = OpenAI()

def get_calories_and_glucose_from_image(image_path, language='en'):
    with open(image_path, "rb") as image:
        base64_image = base64.b64encode(image.read()).decode("utf-8")

    # Language-specific system prompts
    system_prompts = {
        'en': """You are a dietitian. Analyze the meal image for calories and glucose impact. Use this JSON format:
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
}""",
        'fr': """Vous êtes diététicien. Analysez l'image du repas pour les calories et l'impact sur le glucose. Utilisez ce format JSON:
{
    "reasoning": "raisonnement pour les calculs",
    "food_items": [
        {
            "name": "nom de l'aliment",
            "calories": "calories dans l'aliment",
            "glucose_impact": "faible/moyen/élevé"
        }
    ],
    "total": "total des calories du repas",
    "glucose_assessment": {
        "impact_level": "faible/moyen/élevé",
        "explanation": "explication de l'impact sur le glucose",
        "estimated_glucose_rise": "augmentation estimée du glucose en mg/dL"
    }
}""",
        'tr': """Bir diyetisyensiniz. Yemek görüntüsünü kalori ve glukoz etkisi için analiz edin. Bu JSON formatını kullanın:
{
    "reasoning": "hesaplamalar için gerekçelendirme",
    "food_items": [
        {
            "name": "yiyecek adı",
            "calories": "yiyecekteki kalori miktarı",
            "glucose_impact": "düşük/orta/yüksek"
        }
    ],
    "total": "yemekteki toplam kalori",
    "glucose_assessment": {
        "impact_level": "düşük/orta/yüksek",
        "explanation": "glukoz etkisinin açıklaması",
        "estimated_glucose_rise": "tahmini glukoz yükselişi mg/dL"
    }
}"""
    }

    # User prompts in different languages
    user_prompts = {
        'en': "Analyze this meal for calories and glucose impact",
        'fr': "Analysez ce repas pour les calories et l'impact sur le glucose",
        'tr': "Bu yemeği kalori ve glukoz etkisi için analiz edin"
    }

    # Use default English if language not supported
    system_prompt = system_prompts.get(language, system_prompts['en'])
    user_prompt = user_prompts.get(language, user_prompts['en'])

    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_prompt
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
    language = sys.argv[2] if len(sys.argv) > 2 else 'en'
    result = get_calories_and_glucose_from_image(image_path, language)
    print(json.dumps(result, indent=4))