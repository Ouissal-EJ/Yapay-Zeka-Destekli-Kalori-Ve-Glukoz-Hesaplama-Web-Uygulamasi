def get_health_advice(calories: int, language: str = 'en') -> str:
    """Generate health advice based on calorie content."""
    if calories > 800:
        level = 'high'
        calories_to_burn = int(calories * 0.3)  # Recommend burning 30% of calories
    elif calories > 500:
        level = 'medium'
        calories_to_burn = int(calories * 0.2)
    else:
        level = 'low'
        calories_to_burn = 0
    
    from translations import TRANSLATIONS
    advice = TRANSLATIONS[language]['health_advice'][level]
    
    if calories_to_burn:
        advice = advice.format(calories_to_burn=calories_to_burn)
    
    return advice