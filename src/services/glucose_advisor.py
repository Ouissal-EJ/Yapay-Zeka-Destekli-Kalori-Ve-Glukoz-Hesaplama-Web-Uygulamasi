def get_glucose_advice(impact_level: str, glucose_rise: str, language: str = 'en') -> str:
    """Generate health advice based on glucose impact."""
    advice_translations = {
        'en': {
            'high': f"""High glucose impact detected. Recommendations:
• Consider taking a 15-minute walk after eating
• Pair this meal with fiber-rich vegetables
• Stay hydrated
• Monitor blood sugar levels
Expected glucose rise: {glucose_rise}""",
            'medium': f"""Moderate glucose impact. Suggestions:
• Light activity after eating can help
• Balance with protein and healthy fats
• Monitor your response
Expected glucose rise: {glucose_rise}""",
            'low': f"""Low glucose impact - good choice! Tips:
• Continue monitoring as usual
• This meal should have minimal effect on blood sugar
Expected glucose rise: {glucose_rise}"""
        },
        'fr': {
            'high': f"""Impact élevé sur la glycémie. Recommandations:
• Envisagez une promenade de 15 minutes après le repas
• Associez ce repas à des légumes riches en fibres
• Restez hydraté
• Surveillez votre glycémie
Hausse de glucose prévue: {glucose_rise}""",
            'medium': f"""Impact modéré sur la glycémie. Suggestions:
• Une activité légère après le repas peut aider
• Équilibrez avec des protéines et des graisses saines
• Surveillez votre réaction
Hausse de glucose prévue: {glucose_rise}""",
            'low': f"""Faible impact sur la glycémie - bon choix! Conseils:
• Continuez la surveillance habituelle
• Ce repas devrait avoir un effet minimal sur la glycémie
Hausse de glucose prévue: {glucose_rise}"""
        },
        'tr': {
            'high': f"""Yüksek glukoz etkisi tespit edildi. Öneriler:
• Yemekten sonra 15 dakikalık yürüyüş yapın
• Bu öğünü lifli sebzelerle eşleştirin
• Bol su için
• Kan şekeri seviyelerinizi takip edin
Beklenen glukoz yükselişi: {glucose_rise}""",
            'medium': f"""Orta düzey glukoz etkisi. Öneriler:
• Yemekten sonra hafif aktivite faydalı olabilir
• Protein ve sağlıklı yağlarla dengeleyin
• Tepkinizi izleyin
Beklenen glukoz yükselişi: {glucose_rise}""",
            'low': f"""Düşük glukoz etkisi - iyi seçim! İpuçları:
• Normal takibinize devam edin
• Bu öğünün kan şekerine etkisi minimal olmalı
Beklenen glukoz yükselişi: {glucose_rise}"""
        }
    }
    
    return advice_translations.get(language, advice_translations['en']).get(impact_level.lower(), advice_translations['en']['medium'])