export interface ComponentObject {
    id: number
    componentNumber: number
    color: string
    climate: {
        temperature: number
        humidity: number
    }
    createdAt: Date;
}
