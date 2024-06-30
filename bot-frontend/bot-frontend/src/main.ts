import './style.css'

import mqtt from "mqtt";
import {DatabaseComponentObject} from "./types.ts";

const client = mqtt.connect("ws://82.165.106.209:8080");
const mqttTopic = "DeNiLo-Dobot"

export const handleSendTestData = async () => {
    client.publish(mqttTopic, "Hello mqtt");
}

const temperatureSpan = document.getElementById("temperatureSpan")
const humiditySpan = document.getElementById("humiditySpan")
const cubeColorSpan = document.getElementById("colorSpan")

client.on("connect", (event) => {
    console.log(event)
    console.log("connected mqtt")
    client.subscribe(mqttTopic, (err) => {
        // if (err) {
        //     return console.error(err);
        // }
        console.log("subscribed to presence")

    });
});

client.on("message", (topic, message) => {
    // message is Buffer
    if (topic === mqttTopic) {
        const parsed = JSON.parse(message.toString()) as DatabaseComponentObject;
        humiditySpan!.innerText = `${parsed.climate.humidity.toString()}%`
        temperatureSpan!.innerText = `${parsed.climate.temperature.toString()}°C`
        cubeColorSpan!.innerText = parsed.color
    }
});

client.on("error", (err) => {
    console.error("error: ", err);
    client.end()
})

handleSendTestData()

console.log("Moin")