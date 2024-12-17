import { Entry } from '../models/Entry';
import { GlucoseEntry } from '../models/GlucoseEntry';

export class StorageService {
    private static ENTRIES_KEY = 'calorie_entries';
    private static GLUCOSE_KEY = 'glucose_entries';

    static saveEntry(entry: Entry): void {
        const entries = this.getEntries();
        entries.push(entry);
        localStorage.setItem(this.ENTRIES_KEY, JSON.stringify(entries));
    }

    static getEntries(): Entry[] {
        const entriesJson = localStorage.getItem(this.ENTRIES_KEY) || '[]';
        const entries = JSON.parse(entriesJson);
        return entries.map((entry: any) => ({
            ...entry,
            timestamp: new Date(entry.timestamp)
        }));
    }

    static saveGlucoseEntry(entry: GlucoseEntry): void {
        const entries = this.getGlucoseEntries();
        entries.push(entry);
        localStorage.setItem(this.GLUCOSE_KEY, JSON.stringify(entries));
    }

    static getGlucoseEntries(): GlucoseEntry[] {
        const entriesJson = localStorage.getItem(this.GLUCOSE_KEY) || '[]';
        const entries = JSON.parse(entriesJson);
        return entries.map((entry: any) => new GlucoseEntry(
            entry.value,
            new Date(entry.timestamp),
            entry.mealType
        ));
    }

    static clearAll(): void {
        localStorage.removeItem(this.ENTRIES_KEY);
        localStorage.removeItem(this.GLUCOSE_KEY);
    }
}
