export interface DatabaseComponentObject {
    id: string
    componentNumber: number
    color: string
    climate: {
        temperature: number
        humidity: number
    }
    createdAt: Date;
}
