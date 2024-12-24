import React from 'react';
import { useTranslation } from '../hooks/useTranslation';

interface CalorieAdviceProps {
  calories: number;
}

export const CalorieAdvice: React.FC<CalorieAdviceProps> = ({ calories }) => {
  const { t } = useTranslation();

  const getAdvice = () => {
    if (calories > 800) {
      return t('calorie_advice.high', { calories_to_burn: Math.round(calories * 0.3) });
    } else if (calories > 500) {
      return t('calorie_advice.medium');
    }
    return t('calorie_advice.low');
  };

  return (
    <div className="advice-section">
      <h3 className="text-lg font-semibold mb-2">{t('calorie_advice.title')}</h3>
      <p className="text-gray-700 whitespace-pre-line">{getAdvice()}</p>
    </div>
  );
};