import {MongoClient, ObjectId} from "mongodb";
import {DatabaseComponentObject, ICreateComponentObjectDto} from "./types";

export class MongoService {
    constructor(private mongoClient: MongoClient, private databaseName: string, private collectionName: string) {
    }

    private db = this.mongoClient.db(this.databaseName);
    private collection = this.db.collection(this.collectionName)

    async connect() {
        await this.mongoClient.connect()
    }

    async insertComponent(data: ICreateComponentObjectDto) {
        const lastEntry = await this.collection.find({}).sort({$natural: -1}).limit(1).toArray();

        const insertData: DatabaseComponentObject = {
            id: new ObjectId(), ...data,
            createdAt: new Date(),
            componentNumber: 1
        }

        if (lastEntry[0] !== undefined) {
            insertData.componentNumber = lastEntry[0].componentNumber + 1

        }
        await this.collection.insertOne(insertData)
    }

    async getAllComponents() {
        return await this.collection.find().toArray();
    }
}