document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('uploadForm');
    const fileInput = uploadForm.querySelector('input[type="file"]');
    const fileNameDisplay = document.querySelector('.selected-file-name');

    fileInput.addEventListener('change', function(e) {
        const fileName = e.target.files[0]?.name || getTranslation('no_file_selected');
        fileNameDisplay.textContent = fileName;
    });

    uploadForm.onsubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        formData.append('language', currentLang);
        
        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });
            
            if (!response.ok) {
                throw new Error(getTranslation('error_analyzing'));
            }

            const data = await response.json();
            updateResults(data);
        } catch (error) {
            console.error('Error:', error);
            alert(getTranslation('error_analyzing'));
        }
    };
});

function updateResults(data) {
    const results = document.getElementById('results');
    results.style.display = 'grid';
    results.classList.add('visible');

    // Update calorie information
    document.getElementById('totalCalories').textContent = 
        `${data.total} ${getTranslation('calories_unit')}`;

    // Update food items
    const foodItemsHtml = data.food_items.map(item => `
        <div class="food-item">
            <span>${item.name}</span>
            <span>
                ${item.calories} ${getTranslation('calories_unit')}
                <span class="impact-${item.glucose_impact.toLowerCase()}">
                    ● ${translateImpactLevel(item.glucose_impact)}
                </span>
            </span>
        </div>
    `).join('');
    document.getElementById('foodItems').innerHTML = foodItemsHtml;

    // Update glucose information
    document.getElementById('glucoseImpact').textContent = 
        translateImpactLevel(data.glucose_assessment.impact_level);
    document.getElementById('glucoseRise').textContent = 
        `${data.glucose_assessment.estimated_glucose_rise} ${getTranslation('glucose_unit')}`;
    document.getElementById('glucoseExplanation').textContent = 
        data.glucose_assessment.explanation;

    // Update health advice
    document.getElementById('healthAdvice').textContent = data.health_advice;
}