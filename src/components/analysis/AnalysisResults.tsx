import React from 'react';
import { useTranslation } from '../hooks/useTranslation';
import { FoodItemList } from './FoodItemList';
import { CalorieAdvice } from './CalorieAdvice';
import { GlucoseAdvice } from './GlucoseAdvice';

interface AnalysisResultsProps {
  analysis: {
    foodItems: Array<{
      name: string;
      calories: number;
      glucoseImpact: 'low' | 'medium' | 'high';
    }>;
    totalCalories: number;
    glucoseAssessment: {
      impactLevel: 'low' | 'medium' | 'high';
      estimatedGlucoseRise: string;
    };
  };
}

export const AnalysisResults: React.FC<AnalysisResultsProps> = ({ analysis }) => {
  const { t } = useTranslation();

  return (
    <div className="analysis-results grid grid-cols-1 md:grid-cols-2 gap-6">
      <div className="calorie-section">
        <h2 className="text-xl font-bold mb-4">
          📊 {t('calorie_analysis')}
        </h2>
        <FoodItemList items={analysis.foodItems} />
        <div className="total-calories mt-4">
          <h3 className="font-semibold">{t('total_calories')}</h3>
          <p>{analysis.totalCalories}</p>
        </div>
        <CalorieAdvice calories={analysis.totalCalories} />
      </div>

      <div className="glucose-section">
        <h2 className="text-xl font-bold mb-4">
          🌡️ {t('glucose_impact')}
        </h2>
        <div className="glucose-stats mb-4">
          <div className="stat-box">
            <h3 className="font-semibold">{t('impact_level')}</h3>
            <p>{t(`impact_${analysis.glucoseAssessment.impactLevel}`)}</p>
          </div>
          <div className="stat-box">
            <h3 className="font-semibold">{t('expected_rise')}</h3>
            <p>{analysis.glucoseAssessment.estimatedGlucoseRise} {t('glucose_unit')}</p>
          </div>
        </div>
        <GlucoseAdvice 
          impactLevel={analysis.glucoseAssessment.impactLevel}
          glucoseRise={analysis.glucoseAssessment.estimatedGlucoseRise}
        />
      </div>
    </div>
  );
};