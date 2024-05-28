import mqtt from 'mqtt';
import {MongoClient} from 'mongodb'

const MONGO_URL = "mongodb://dobot:15-E101-16@82.165.106.209:27017/?authMechanism=SCRAM-SHA-1&tls=false&authSource=dobot";
const DB_NAME = "dobot";
const COLLECTION_NAME = "dobot"

const client = new MongoClient(MONGO_URL);


async function main() {
    // Use connect method to connect to the server
    await client.connect();
    console.log('Connected successfully to server');
    const db = client.db(DB_NAME);
    const collection = db.collection(COLLECTION_NAME);
    const entries = collection.find();
    console.log(collection.find())

    // the following code examples can be pasted here...

    return 'done.';
}

main()
    .then(console.log)
    .catch(console.error)
    .finally(() => client.close());
