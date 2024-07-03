import {ObjectId} from "mongodb";

export interface ICreateComponentObjectDto {
    color: string
    climate: {
        temperature: number
        humidity: number
    }
    currentEnergyCost: number
}
export interface DatabaseComponentObject {
    id: ObjectId
    componentNumber: number
    color: string
    climate: {
        temperature: number
        humidity: number
    }
    createdAt: Date;
}
