def get_calorie_advice(calories: int, language: str = 'en') -> str:
    """Generate health advice based on calorie content."""
    advice_translations = {
        'en': {
            'high': f"""This meal is high in calories ({calories}). Consider:
• Reducing portion sizes
• Choosing lower-calorie alternatives
• Adding a 30-minute workout to burn approximately {int(calories * 0.3)} calories
• Consider splitting this meal into two portions""",
            'medium': """This is a moderate-calorie meal. To maintain healthy eating:
• Make sure to balance with other meals
• Include vegetables in your meal
• Stay hydrated""",
            'low': "This is a light meal, good for weight management!"
        },
        'fr': {
            'high': f"""Ce repas est riche en calories ({calories}). Considérez:
• Réduire les portions
• Choisir des alternatives moins caloriques
• Ajouter 30 minutes d'exercice pour brûler environ {int(calories * 0.3)} calories
• Envisager de diviser ce repas en deux portions""",
            'medium': """C'est un repas modéré en calories. Pour maintenir une alimentation saine:
• Équilibrez avec les autres repas
• Incluez des légumes dans votre repas
• Restez hydraté""",
            'low': "C'est un repas léger, bon pour la gestion du poids!"
        },
        'tr': {
            'high': f"""Bu yemek yüksek kalorili ({calories}). Öneriler:
• Porsiyon boyutlarını azaltın
• Daha düşük kalorili alternatifler seçin
• Yaklaşık {int(calories * 0.3)} kalori yakmak için 30 dakikalık egzersiz ekleyin
• Bu öğünü iki porsiyona bölmeyi düşünün""",
            'medium': """Bu orta kalorili bir öğün. Sağlıklı beslenmeyi sürdürmek için:
• Diğer öğünlerle dengelediğinizden emin olun
• Öğününüze sebze ekleyin
• Bol su için""",
            'low': "Bu hafif bir öğün, kilo kontrolü için ideal!"
        }
    }

    if calories > 800:
        level = 'high'
    elif calories > 500:
        level = 'medium'
    else:
        level = 'low'
    
    return advice_translations.get(language, advice_translations['en']).get(level)