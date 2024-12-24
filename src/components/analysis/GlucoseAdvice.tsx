import React from 'react';
import { useTranslation } from '../hooks/useTranslation';

interface GlucoseAdviceProps {
  impactLevel: 'low' | 'medium' | 'high';
  glucoseRise: string;
}

export const GlucoseAdvice: React.FC<GlucoseAdviceProps> = ({ impactLevel, glucoseRise }) => {
  const { t } = useTranslation();

  const getAdvice = () => {
    return t(`glucose_advice.${impactLevel}`, { glucose_rise: glucoseRise });
  };

  return (
    <div className="advice-section">
      <h3 className="text-lg font-semibold mb-2">{t('glucose_advice.title')}</h3>
      <p className="text-gray-700 whitespace-pre-line">{getAdvice()}</p>
    </div>
  );
};