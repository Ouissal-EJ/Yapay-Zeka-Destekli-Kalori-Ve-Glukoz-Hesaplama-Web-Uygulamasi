import React, { useState } from 'react';
import { Entry } from '../models/Entry';
import { GlucoseEntry } from '../models/GlucoseEntry';

interface EntryFormProps {
    onSubmit: (entry: Entry) => void;
    onGlucoseSubmit?: (entry: GlucoseEntry) => void;
}

export const EntryForm: React.FC<EntryFormProps> = ({ onSubmit, onGlucoseSubmit }) => {
    const [description, setDescription] = useState('');
    const [calories, setCalories] = useState('');
    const [glucoseValue, setGlucoseValue] = useState<number>(0);
    const [mealType, setMealType] = useState<'before' | 'after'>('before');

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        onSubmit(new Entry(description, Number(calories), new Date()));
        setDescription('');
        setCalories('');
    };

    const handleGlucoseSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (onGlucoseSubmit && glucoseValue > 0) {
            onGlucoseSubmit(new GlucoseEntry(glucoseValue, new Date(), mealType));
            setGlucoseValue(0);
        }
    };

    return (
        <div className="entry-forms">
            <div className="calorie-form">
                <h3>Add Calorie Entry</h3>
                <form onSubmit={handleSubmit}>
                    <input
                        type="text"
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                        placeholder="Description"
                    />
                    <input
                        type="number"
                        value={calories}
                        onChange={(e) => setCalories(e.target.value)}
                        placeholder="Calories"
                    />
                    <button type="submit">Add Entry</button>
                </form>
            </div>

            <div className="glucose-form">
                <h3>Add Glucose Entry</h3>
                <form onSubmit={handleGlucoseSubmit}>
                    <input
                        type="number"
                        value={glucoseValue}
                        onChange={(e) => setGlucoseValue(Number(e.target.value))}
                        placeholder="Blood glucose level"
                    />
                    <select 
                        value={mealType} 
                        onChange={(e) => setMealType(e.target.value as 'before' | 'after')}
                    >
                        <option value="before">Before Meal</option>
                        <option value="after">After Meal</option>
                    </select>
                    <button type="submit">Add Glucose Entry</button>
                </form>
            </div>
        </div>
    );
};
