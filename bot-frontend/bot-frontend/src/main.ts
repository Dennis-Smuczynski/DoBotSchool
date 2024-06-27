import './style.css'

import mqtt from "mqtt";

const client = mqtt.connect("ws://test.mosquitto.org:8080");

document.getElementById("testBtn")!.addEventListener("click", () => {
    handleSendTestData()
})

export const handleSendTestData = async () => {
    client.publish("presence", "Hello mqtt");
}

client.on("connect", (event) => {
    console.log(event)
    console.log("connected mqtt")
    client.subscribe("presence", (err) => {
        // if (err) {
        //     return console.error(err);
        // }
        console.log("subscribed to presence")

    });
});

client.on("message", (topic, message) => {
    // message is Buffer
    console.log(message.toString());
});

client.on("error", (err) => {
    console.error("error: ", err);
    client.end()
})

handleSendTestData()

console.log("Moin")