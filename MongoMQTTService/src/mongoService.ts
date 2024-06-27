import {MongoClient} from "mongodb";
import {ComponentObject} from "./types";

export class MongoService {
    constructor(private mongoClient: MongoClient) { }
    db = this.mongoClient.connect()

    static async insertComponent(data: ComponentObject ) {
        await Promise.resolve()
    }
}