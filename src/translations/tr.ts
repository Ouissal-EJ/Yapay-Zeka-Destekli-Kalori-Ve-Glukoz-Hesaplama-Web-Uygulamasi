export default {
  title: 'Akıllı Yemek Analizi',
  calorie_analysis: 'Kalori Analizi',
  glucose_impact: 'Glukoz Etkisi',
  impact_level: 'Etki Seviyesi',
  expected_rise: 'Beklenen Yükseliş',
  total_calories: 'Toplam Kalori',
  calories_unit: 'kal',
  glucose_unit: 'mg/dL',
  
  impact_low: 'Düşük',
  impact_medium: 'Orta',
  impact_high: 'Yüksek',

  calorie_advice: {
    title: 'Kalori Önerisi',
    high: 'Bu öğün yüksek kalorili. Öneriler:\n- Porsiyon boyutunu azaltın\n- Daha hafif alternatifler seçin\n- {calories_to_burn} kalori yakmak için 30 dakika egzersiz yapın',
    medium: 'Bu öğün orta kalorili. Sağlıklı denge için:\n- Porsiyon kontrolüne dikkat edin\n- Bir sonraki öğününüzde sebze ekleyin\n- 15 dakikalık yürüyüş yapın',
    low: 'Bu öğün sağlıklı kalori aralığında. İyi alışkanlıklarınızı sürdürün!'
  },

  glucose_advice: {
    title: 'Glukoz Önerisi',
    high: 'Glukoz etkisi yüksek. Öneriler:\n- Öğünden sonra 15 dakika yürüyüş yapın\n- Bol su için\n- Bir sonraki öğünde karbonhidrat miktarını azaltın\nTahmini yükseliş: {glucose_rise}',
    medium: 'Glukoz etkisi orta seviyede. Öneriler:\n- Öğünden sonra hafif aktivite yapın\n- Su tüketiminize dikkat edin\nTahmini yükseliş: {glucose_rise}',
    low: 'Glukoz etkisi düşük, harika!\n- Bu dengeli beslenme şeklini sürdürün\nTahmini yükseliş: {glucose_rise}'
  }
};