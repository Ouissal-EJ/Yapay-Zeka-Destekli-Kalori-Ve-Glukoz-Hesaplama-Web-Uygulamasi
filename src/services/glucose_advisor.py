def get_glucose_range(glucose_rise: float) -> str:
    """Categorize glucose impact based on expected glucose rise in mg/dL"""
    if glucose_rise >= 50:
        return 'high'
    elif glucose_rise >= 30:
        return 'medium'
    return 'low'

def get_glucose_advice(glucose_rise: float, language: str = 'en') -> str:
    """Generate health advice based on glucose impact."""
    impact_level = get_glucose_range(float(glucose_rise))
    
    advice_translations = {
        'en': {
            'high': f"""High glucose impact detected (Expected rise: {glucose_rise} mg/dL). Recommendations:
• Consider taking a 15-minute walk after eating
• Pair this meal with fiber-rich vegetables
• Stay hydrated
• Monitor blood sugar levels""",
            'medium': f"""Moderate glucose impact (Expected rise: {glucose_rise} mg/dL). Suggestions:
• Light activity after eating can help
• Balance with protein and healthy fats
• Monitor your response""",
            'low': f"""Low glucose impact (Expected rise: {glucose_rise} mg/dL) - good choice! Tips:
• Continue monitoring as usual
• This meal should have minimal effect on blood sugar"""
        },
        'fr': {
            'high': f"""Impact élevé sur la glycémie (Hausse prévue: {glucose_rise} mg/dL). Recommandations:
• Envisagez une promenade de 15 minutes après le repas
• Associez ce repas à des légumes riches en fibres
• Restez hydraté
• Surveillez votre glycémie""",
            'medium': f"""Impact modéré sur la glycémie (Hausse prévue: {glucose_rise} mg/dL). Suggestions:
• Une activité légère après le repas peut aider
• Équilibrez avec des protéines et des graisses saines
• Surveillez votre réaction""",
            'low': f"""Faible impact sur la glycémie (Hausse prévue: {glucose_rise} mg/dL) - bon choix! Conseils:
• Continuez la surveillance habituelle
• Ce repas devrait avoir un effet minimal sur la glycémie"""
        },
        'tr': {
            'high': f"""Yüksek glukoz etkisi tespit edildi (Beklenen yükseliş: {glucose_rise} mg/dL). Öneriler:
• Yemekten sonra 15 dakikalık yürüyüş yapın
• Bu öğünü lifli sebzelerle eşleştirin
• Bol su için
• Kan şekeri seviyelerinizi takip edin""",
            'medium': f"""Orta düzey glukoz etkisi (Beklenen yükseliş: {glucose_rise} mg/dL). Öneriler:
• Yemekten sonra hafif aktivite faydalı olabilir
• Protein ve sağlıklı yağlarla dengeleyin
• Tepkinizi izleyin""",
            'low': f"""Düşük glukoz etkisi (Beklenen yükseliş: {glucose_rise} mg/dL) - iyi seçim! İpuçları:
• Normal takibinize devam edin
• Bu öğünün kan şekerine etkisi minimal olmalı"""
        }
    }
    
    return advice_translations.get(language, advice_translations['en']).get(impact_level, advice_translations['en']['medium'])