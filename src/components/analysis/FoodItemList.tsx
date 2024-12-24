import React from 'react';
import { useTranslation } from '../hooks/useTranslation';

interface FoodItem {
  name: string;
  calories: number;
  glucoseImpact: 'low' | 'medium' | 'high';
}

interface FoodItemListProps {
  items: FoodItem[];
}

export const FoodItemList: React.FC<FoodItemListProps> = ({ items }) => {
  const { t } = useTranslation();

  return (
    <div className="food-items">
      {items.map((item, index) => (
        <div key={index} className="food-item flex justify-between items-center py-2">
          <span>{item.name}</span>
          <span>
            {item.calories} {t('calories_unit')}
            <span className={`impact-${item.glucoseImpact} ml-2`}>
              ● {t(`impact_${item.glucoseImpact}`)}
            </span>
          </span>
        </div>
      ))}
    </div>
  );
};