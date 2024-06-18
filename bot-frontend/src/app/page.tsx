import mqtt from "mqtt";

const client = mqtt.connect("ws://test.mosquitto.org:8080");
export default function Home() {
    // ws://test.mosquitto.org:8080

    const handleSendTestData = () => {
        client.publish("presence", "Hello mqtt");
    }

    client.on("connect", (event) => {
        console.log(event)
        console.log("connected mqtt")
        client.subscribe("presence", (err) => {
            if (err) {
                return console.error(err);
            }
            console.log("subscribed to presence")

        });
    });

    client.on("message", (topic, message) => {
        // message is Buffer
        console.log(message.toString());
        client.end();
    });

    client.on("error", (err) => {
        console.error("error: ", err);
    })

    handleSendTestData()

    return (
        <div className={"d-flex justify-content-center align-items-center"}>
            Temperatur:
            Luftfeuchtigkeit:
            <button onClick={handleSendTestData}>test</button>
            {/*<Button onClick={handleSendTestData}>Send test data</Button>*/}
        </div>
    );
}
