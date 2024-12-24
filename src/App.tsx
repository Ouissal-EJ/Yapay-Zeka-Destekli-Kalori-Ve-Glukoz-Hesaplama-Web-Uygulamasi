import React, { useState, useEffect } from 'react';
import { Entry } from './models/Entry';
import { GlucoseEntry } from './models/GlucoseEntry';
import { EntryForm } from './components/EntryForm';
import { StorageService } from './services/StorageService';
import { HealthAdviceService } from './services/HealthAdviceService';

export const App: React.FC = () => {
    const [activeView, setActiveView] = useState<'calories' | 'health'>('calories');
    const [entries, setEntries] = useState<Entry[]>([]);
    const [glucoseEntries, setGlucoseEntries] = useState<GlucoseEntry[]>([]);
    const [imageUrl, setImageUrl] = useState<string>('');
    const [calories, setCalories] = useState<number | null>(null);

    // Load both types of entries on component mount
    useEffect(() => {
        const loadEntries = () => {
            const calorieEntries = StorageService.getEntries();
            const glucoseData = StorageService.getGlucoseEntries();
            
            setEntries(calorieEntries);
            setGlucoseEntries(glucoseData);
            
            console.log('Loaded glucose entries:', glucoseData); // Debug log
        };

        loadEntries();
    }, []);

    const handleSubmit = (entry: Entry) => {
        StorageService.saveEntry(entry);
        setEntries(StorageService.getEntries());
    };

    const handleGlucoseSubmit = (entry: GlucoseEntry) => {
        StorageService.saveGlucoseEntry(entry);
        setGlucoseEntries(StorageService.getGlucoseEntries());
    };

    const handleImageUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
        const file = event.target.files?.[0];
        if (file) {
            const formData = new FormData();
            formData.append('file', file);

            try {
                const response = await fetch('/predict', {
                    method: 'POST',
                    body: formData,
                });
                const data = await response.json();
                setCalories(data.calories);
                setImageUrl(URL.createObjectURL(file));
            } catch (error) {
                console.error('Error:', error);
            }
        }
    };

    return (
        <div className="app">
            <nav className="app-nav">
                <button 
                    onClick={() => setActiveView('calories')}
                    className={activeView === 'calories' ? 'active' : ''}
                >
                    Calorie Counter
                </button>
                <button 
                    onClick={() => setActiveView('health')}
                    className={activeView === 'health' ? 'active' : ''}
                >
                    Health Tracker
                </button>
            </nav>

            {activeView === 'calories' ? (
                <div className="calorie-counter">
                    <h1>Calorie Counter</h1>
                    <p>Upload a meal image to calculate its calories</p>
                    <input
                        type="file"
                        accept="image/*"
                        onChange={handleImageUpload}
                    />
                    {imageUrl && <img src={imageUrl} alt="Uploaded meal" style={{ maxWidth: '300px' }} />}
                    {calories && (
                        <div className="advice-section">
                            <p>Estimated calories: {calories}</p>
                            <p className="health-advice">{HealthAdviceService.getCalorieAdvice(calories)}</p>
                        </div>
                    )}
                </div>
            ) : (
                <div className="health-tracker">
                    <h1>Health Tracker</h1>
                    <EntryForm onSubmit={handleSubmit} onGlucoseSubmit={handleGlucoseSubmit} />
                    <div className="entries-container">
                        <div className="calorie-entries">
                            <h3>Calorie Entries</h3>
                            {entries.map((entry, index) => (
                                <div key={index} className="entry">
                                    <div>
                                        <span>{entry.description}: {entry.calories} calories</span>
                                        <span>({new Date(entry.timestamp).toLocaleString()})</span>
                                        <div className="advice">
                                            {HealthAdviceService.getCalorieAdvice(entry.calories)}
                                        </div>
                                    </div>
                                </div>
                            ))}
                        </div>

                        <div className="glucose-entries">
                            <h3>Glucose Entries</h3>
                            {glucoseEntries.map((entry, index) => (
                                <div key={index} className="entry">
                                    <div>
                                        <span>{entry.value} mg/dL - {entry.mealType} meal</span>
                                        <span>({new Date(entry.timestamp).toLocaleString()})</span>
                                        <div className="advice">
                                            {HealthAdviceService.getGlucoseAdvice(entry.value, entry.mealType)}
                                        </div>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};
