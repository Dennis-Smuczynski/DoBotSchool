import {DataType, OPCUAServer, Variant} from "node-opcua";

// import sensor from "node-dht-sensor";

const server = new OPCUAServer({
    port: 4334, // the port of the listening socket of the server
    resourcePath: "/UA/MyLittleServer", // this path will be added to the endpoint resource name
});

async function handleOPCUAServer() {
    await server.initialize();
    console.log("Initialized")

    const addressSpace = server.engine.addressSpace;
    if (!addressSpace) {
        await server.shutdown();
        throw new Error("Kurwa");
    }
    const namespace = addressSpace.getOwnNamespace();
    const device = namespace.addObject({
        organizedBy: addressSpace.rootFolder.objects,
        browseName: "ClimateSensor"
    })

    const temperature = (await getTemperatureAndHumidity()).temp;
    const humidity = (await getTemperatureAndHumidity()).humidity;

    namespace.addVariable({
        componentOf: device,
        browseName: "temperature",
        dataType: "String",
        value: {
            get:  () => new Variant({dataType: DataType.String, value: temperature})
        }
    });

    namespace.addVariable({
        componentOf: device,
        browseName: "humidity",
        dataType: "String",
        value: {
            get:  () => new Variant({dataType: DataType.String, value: humidity})
        }
    });

    await server.start();


    console.log("Server is now listening ... ( press CTRL+C to stop) ");
    await new Promise((resolve) => process.once("SIGINT", resolve));

    await server.shutdown();
}

handleOPCUAServer()

async function getTemperatureAndHumidity() {
    try {
        // const res = await sensor.read(22, 4);
        const res = {temperature: 50, humidity: 60}
        return {
            temp: `${res.temperature.toFixed(1)}`,
            humidity: `${res.humidity.toFixed(1)}`
        }
    } catch (err) {
        console.error("Failed to read sensor data:", err);
        return {
            temp: `-0`,
            humidity: `-0`
        }
    }
}