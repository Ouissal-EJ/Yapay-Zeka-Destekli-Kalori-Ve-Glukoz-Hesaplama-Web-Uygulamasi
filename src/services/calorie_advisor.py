def get_calorie_advice(calories: int, language: str = 'en') -> str:
    """Generate health advice based on calorie content."""
    def get_calorie_level(cal: int) -> str:
        if cal > 1000:
            return 'very_high'
        elif cal > 800:
            return 'high'
        elif cal > 500:
            return 'medium'
        elif cal > 300:
            return 'low'
        return 'very_low'

    advice_translations = {
        'en': {
            'very_high': f"""This meal is extremely high in calories ({calories}). Warning:
• This exceeds recommended calories per meal
• Consider splitting into 2-3 smaller portions
• Would need {int(calories * 0.4)} minutes of intense exercise
• Consult with a nutritionist for meal planning""",
            'high': f"""This meal is high in calories ({calories}). Consider:
• Reducing portion sizes
• Choosing lower-calorie alternatives
• Adding a 30-minute workout to burn approximately {int(calories * 0.3)} calories
• Consider splitting this meal into two portions""",
            'medium': """This is a moderate-calorie meal. To maintain healthy eating:
• Make sure to balance with other meals
• Include vegetables in your meal
• Stay hydrated""",
            'low': "This is a light meal, good for weight management!",
            'very_low': "This is a very light meal, excellent for weight management!"
        },
        'fr': {
            'very_high': f"""Ce repas est extrêmement riche en calories ({calories}). Attention:
• Cela dépasse les calories recommandées par repas
• Envisagez de diviser en 2-3 portions plus petites
• Nécessiterait {int(calories * 0.4)} minutes d'exercice intense
• Consultez un nutritionniste pour la planification des repas""",
            'high': f"""Ce repas est riche en calories ({calories}). Considérez:
• Réduire les portions
• Choisir des alternatives moins caloriques
• Ajouter 30 minutes d'exercice pour brûler environ {int(calories * 0.3)} calories
• Envisager de diviser ce repas en deux portions""",
            'medium': """C'est un repas modéré en calories. Pour maintenir une alimentation saine:
• Équilibrez avec les autres repas
• Incluez des légumes dans votre repas
• Restez hydraté""",
            'low': "C'est un repas léger, bon pour la gestion du poids!",
            'very_low': "C'est un repas très léger, excellent pour la gestion du poids!"
        },
        'tr': {
            'very_high': f"""Bu öğün aşırı yüksek kalorili ({calories}). Uyarı:
• Öğün başına önerilen kalori miktarını aşıyor
• 2-3 küçük porsiyona bölmeyi düşünün
• {int(calories * 0.4)} dakika yoğun egzersiz gerektirir
• Öğün planlaması için bir diyetisyene danışın""",
            'high': f"""Bu yemek yüksek kalorili ({calories}). Öneriler:
• Porsiyon boyutlarını azaltın
• Daha düşük kalorili alternatifler seçin
• Yaklaşık {int(calories * 0.3)} kalori yakmak için 30 dakikalık egzersiz ekleyin
• Bu öğünü iki porsiyona bölmeyi düşünün""",
            'medium': """Bu orta kalorili bir öğün. Sağlıklı beslenmeyi sürdürmek için:
• Diğer öğünlerle dengelediğinizden emin olun
• Öğününüze sebze ekleyin
• Bol su için""",
            'low': "Bu hafif bir öğün, kilo kontrolü için ideal!",
            'very_low': "Bu çok hafif bir öğün, kilo kontrolü için mükemmel!"
        }
    }
    
    level = get_calorie_level(calories)
    return advice_translations.get(language, advice_translations['en']).get(level, advice_translations['en']['medium'])