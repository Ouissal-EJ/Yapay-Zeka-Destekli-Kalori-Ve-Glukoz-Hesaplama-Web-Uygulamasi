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
        'en': """You are a dietitian. Analyze the meal image for calories and glucose impact using these specific ranges:

Calorie Categories:
- Very High: > 1000 calories
- High: 801-1000 calories
- Medium: 501-800 calories
- Low: 301-500 calories
- Very Low: ≤ 300 calories

Glucose Impact Categories (Expected Blood Glucose Rise):
- High: ≥ 50 mg/dL rise
- Medium: 30-49 mg/dL rise
- Low: < 30 mg/dL rise

Use this JSON format:
{
    "reasoning": "reasoning for the calculations",
    "food_items": [
        {
            "name": "food item name",
            "calories": "calories in the food item",
            "glucose_impact": "low/medium/high based on above ranges"
        }
    ],
    "total": "total calories in the meal",
    "glucose_assessment": {
        "impact_level": "low/medium/high strictly based on above ranges",
        "explanation": "explanation of glucose impact",
        "estimated_glucose_rise": "numeric value in mg/dL"
    },
    "health_advice": "detailed advice based on the analysis"
}""",
        'fr': """Vous êtes diététicien. Analysez l'image du repas en utilisant ces plages spécifiques:

Catégories de calories:
- Très élevé: > 1000 calories
- Élevé: 801-1000 calories
- Moyen: 501-800 calories
- Faible: 301-500 calories
- Très faible: ≤ 300 calories

Catégories d'impact sur le glucose (Augmentation attendue):
- Élevé: ≥ 50 mg/dL
- Moyen: 30-49 mg/dL
- Faible: < 30 mg/dL

Utilisez ce format JSON:
{
    "reasoning": "raisonnement pour les calculs",
    "food_items": [
        {
            "name": "nom de l'aliment",
            "calories": "calories dans l'aliment",
            "glucose_impact": "faible/moyen/élevé basé sur les plages ci-dessus"
        }
    ],
    "total": "total des calories du repas",
    "glucose_assessment": {
        "impact_level": "faible/moyen/élevé strictement basé sur les plages ci-dessus",
        "explanation": "explication de l'impact sur le glucose",
        "estimated_glucose_rise": "valeur numérique en mg/dL"
    },
    "health_advice": "conseils détaillés basés sur l'analyse"
}""",
        'tr': """Bir diyetisyensiniz. Yemek görüntüsünü bu özel aralıkları kullanarak analiz edin:

Kalori Kategorileri:
- Çok Yüksek: > 1000 kalori
- Yüksek: 801-1000 kalori
- Orta: 501-800 kalori
- Düşük: 301-500 kalori
- Çok Düşük: ≤ 300 kalori

Glukoz Etki Kategorileri (Beklenen Kan Şekeri Yükselişi):
- Yüksek: ≥ 50 mg/dL
- Orta: 30-49 mg/dL
- Düşük: < 30 mg/dL

Bu JSON formatını kullanın:
{
    "reasoning": "hesaplamalar için gerekçelendirme",
    "food_items": [
        {
            "name": "yiyecek adı",
            "calories": "yiyecekteki kalori miktarı",
            "glucose_impact": "düşük/orta/yüksek yukarıdaki aralıklara göre"
        }
    ],
    "total": "yemekteki toplam kalori",
    "glucose_assessment": {
        "impact_level": "düşük/orta/yüksek yukarıdaki aralıklara göre",
        "explanation": "glukoz etkisinin açıklaması",
        "estimated_glucose_rise": "sayısal değer mg/dL cinsinden"
    },
    "health_advice": "analize dayalı ayrıntılı öneriler"
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