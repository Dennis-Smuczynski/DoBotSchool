import mqtt from 'mqtt';
import {MongoClient, ObjectId} from 'mongodb'
import express from 'express'
import {MongoService} from "./mongoService";

const MONGO_URL = "mongodb://127.0.0.1:27017";
const DB_NAME = "test";
const COLLECTION_NAME = "dobot"

const MQTT_TOPIC = "DeNiLo-Dobot";

const mongoClient = new MongoClient(MONGO_URL);
const mqttClient = mqtt.connect("mqtt://82.165.106.209:1883");

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
    .finally(() => mongoClient.close());


app.post('/component', async (req, res) => {
    const data = req.body;
    console.log(data);

    await MongoService.insertComponent(data)
    mqttClient.publish(MQTT_TOPIC, JSON.stringify({test: data.test}))
    return res.status(200).json({})
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})

mqttClient.on("connect", () => {
    console.log("connect4ed to mqtt")
    mqttClient.subscribe("presence", (err) => {
        if (!err) {
            mqttClient.publish("presence", "Hello mqtt");
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
    await mongoClient.connect()
    console.log("Successfully connected to mongodb")
}



