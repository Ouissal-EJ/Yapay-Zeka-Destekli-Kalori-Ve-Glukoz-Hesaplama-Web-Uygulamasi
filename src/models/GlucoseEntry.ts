export class GlucoseEntry {
    constructor(
        public readonly value: number,
        public readonly timestamp: Date,
        public readonly mealType: 'before' | 'after'
    ) {}

    static fromJSON(json: any): GlucoseEntry {
        return new GlucoseEntry(
            json.value,
            new Date(json.timestamp),
            json.mealType
        );
    }

    toJSON() {
        return {
            value: this.value,
            timestamp: this.timestamp,
            mealType: this.mealType
        };
    }
}
