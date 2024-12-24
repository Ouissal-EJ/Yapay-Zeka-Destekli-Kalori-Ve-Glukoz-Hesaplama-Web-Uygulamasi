export class HealthAdviceService {
    static getCalorieAdvice(calories: number): string {
        if (calories > 800) {
            return `This meal is high in calories (${calories}). Consider:
                • Reducing portion size
                • Choose lower-calorie alternatives
                • You would need ${Math.round(calories/7.7)} minutes of running to burn these calories
                • Consider splitting this meal into two portions`;
        } else if (calories > 500) {
            return `This is a moderate-calorie meal. To maintain healthy eating:
                • Make sure to balance with other meals
                • Include vegetables in your meal
                • Stay hydrated`;
        }
        return "This is a light meal, good for weight management!";
    }

    static getGlucoseAdvice(value: number, mealType: 'before' | 'after'): string {
        if (mealType === 'before') {
            if (value > 130) {
                return `Your pre-meal glucose is high (${value} mg/dL). Recommendations:
                    • Consult your healthcare provider
                    • Consider light exercise before meals
                    • Stay hydrated
                    • Monitor carbohydrate intake`;
            } else if (value < 70) {
                return `Your pre-meal glucose is low (${value} mg/dL). Consider:
                    • Having a small snack
                    • Monitor for symptoms of hypoglycemia
                    • Consult your healthcare provider`;
            }
        } else {
            if (value > 180) {
                return `Your post-meal glucose is high (${value} mg/dL). Suggestions:
                    • Take a 15-minute walk
                    • Stay hydrated
                    • Review meal composition
                    • Consider timing of medications`;
            } else if (value < 70) {
                return `Your post-meal glucose is low (${value} mg/dL). Consider:
                    • Having a fast-acting carbohydrate
                    • Review medication timing
                    • Consult your healthcare provider`;
            }
        }
        return "Your glucose levels are within normal range. Keep up the good work!";
    }
}
