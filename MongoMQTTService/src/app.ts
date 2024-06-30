import mqtt, {MqttClient} from 'mqtt';
import {MongoClient, ObjectId} from 'mongodb'
import express from 'express'
import {MongoService} from "./mongoService";
import { ICreateComponentObjectDto} from "./types";

const MONGO_URL = "mongodb://127.0.0.1:27017";
const DB_NAME = "test";
const COLLECTION_NAME = "dobot"

const MQTT_TOPIC = "DeNiLo-Dobot"; // DeNiLo-Dobot

const mongoClient = new MongoClient(MONGO_URL);
const mqttClient: MqttClient = mqtt.connect("mqtt://127.0.0.1:1883");
const mongoService = new MongoService(mongoClient, DB_NAME, COLLECTION_NAME);

const app = express()
const port = 3000

app.use((req, res, next) => {
    res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    res.header('Access-Control-Allow-Origin', '*');
    res.header(
        'Access-Control-Allow-Methods',
        'GET, POST, PUT, DELETE, OPTIONS'
    );
    next();
});


// JSON parser
app.use(express.json({ limit: "50mb" }));
app.use(express.urlencoded({ limit: "50mb", extended: true, parameterLimit: 50000 }));


main()
    .then(console.log)
    .catch(console.error)


app.post('/component', async (req, res) => {
    const data = req.body as ICreateComponentObjectDto;

    mqttClient.publish(MQTT_TOPIC, JSON.stringify(data))
    await mongoService.insertComponent(data);
    
    return res.status(200).json({})
})

app.get('/components', async (req, res) => {
   const mongoData = await mongoService.getAllComponents()
    return res.status(200).json(mongoData);
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})

mqttClient.on("connect", () => {
    console.log("connect4ed to mqtt")
    mqttClient.subscribe(MQTT_TOPIC, (err) => {
        if (!err) {
            mqttClient.publish(MQTT_TOPIC, "Hello mqtt");
        }
    });
});

mqttClient.on("message", (topic, message) => {
    // message is Buffer
    console.log(message.toString());
    // mqttClient.end();
});

mqttClient.on("error", (error) => {
    console.log(error);
})

async function main() {
    await mongoService.connect()
    console.log("Successfully connected to mongodb")
}



