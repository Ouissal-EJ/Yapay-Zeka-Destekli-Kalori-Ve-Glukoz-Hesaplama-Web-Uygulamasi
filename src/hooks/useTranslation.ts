import { useContext } from 'react';
import { LanguageContext } from '../contexts/LanguageContext';

export const useTranslation = () => {
  const { language, translations } = useContext(LanguageContext);

  const t = (key: string, params: Record<string, any> = {}) => {
    const keys = key.split('.');
    let value = translations[language];
    
    for (const k of keys) {
      value = value?.[k];
    }

    if (typeof value === 'string') {
      return Object.entries(params).reduce(
        (str, [key, val]) => str.replace(`{${key}}`, val),
        value
      );
    }

    return key;
  };

  return { t, language };
};