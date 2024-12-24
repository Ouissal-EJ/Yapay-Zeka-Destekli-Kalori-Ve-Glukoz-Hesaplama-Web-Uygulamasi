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
        'en': """You are a dietitian. Analyze the meal image for calories, glucose impact, and provide personalized health advice. Use this JSON format:
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
    },
    "health_advice": "detailed, personalized health advice based on the meal content, including specific recommendations for portion control, alternative ingredients, exercise suggestions, and timing of the meal"
}""",
        'fr': """Vous êtes diététicien. Analysez l'image du repas pour les calories, l'impact sur le glucose et fournissez des conseils santé personnalisés. Utilisez ce format JSON:
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
    },
    "health_advice": "conseils santé détaillés et personnalisés basés sur le contenu du repas, incluant des recommandations spécifiques pour le contrôle des portions, les ingrédients alternatifs, les suggestions d'exercice et le moment du repas"
}""",
        'tr': """Bir diyetisyensiniz. Yemek görüntüsünü kalori, glukoz etkisi için analiz edin ve kişiselleştirilmiş sağlık önerileri sunun. Bu JSON formatını kullanın:
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
    },
    "health_advice": "yemek içeriğine dayalı ayrıntılı, kişiselleştirilmiş sağlık önerileri, porsiyon kontrolü, alternatif malzemeler, egzersiz önerileri ve öğün zamanlaması için özel tavsiyeler içerir"
}"""
    }

    # User prompts in different languages
    user_prompts = {
        'en': "Analyze this meal for calories, glucose impact, and provide personalized health advice",
        'fr': "Analysez ce repas pour les calories, l'impact sur le glucose et donnez des conseils santé personnalisés",
        'tr': "Bu yemeği kalori, glukoz etkisi için analiz edin ve kişiselleştirilmiş sağlık önerileri verin"
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