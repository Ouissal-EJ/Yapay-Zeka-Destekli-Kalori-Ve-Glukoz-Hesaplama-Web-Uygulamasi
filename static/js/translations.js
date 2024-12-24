const translations = {{ translations|tojson|safe }};
let currentLang = '{{ lang|default("en") }}';

function changeLanguage(lang) {
    if (lang !== currentLang) {
        window.location.href = `/?lang=${lang}`;
    }
}

function getTranslation(key, defaultValue = '') {
    return translations[key] || defaultValue;
}

function translateImpactLevel(level) {
    return translations[`impact_${level.toLowerCase()}`] || level;
}