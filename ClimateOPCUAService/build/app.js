"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
const node_opcua_1 = require("node-opcua");
// import sensor from "node-dht-sensor";
const server = new node_opcua_1.OPCUAServer({
    port: 4334, // the port of the listening socket of the server
    resourcePath: "/UA/MyLittleServer", // this path will be added to the endpoint resource name
});
function handleOPCUAServer() {
    return __awaiter(this, void 0, void 0, function* () {
        yield server.initialize();
        console.log("Initialized");
        const addressSpace = server.engine.addressSpace;
        if (!addressSpace) {
            yield server.shutdown();
            throw new Error("Kurwa");
        }
        const namespace = addressSpace.getOwnNamespace();
        const device = namespace.addObject({
            organizedBy: addressSpace.rootFolder.objects,
            browseName: "ClimateSensor"
        });
        const temperature = (yield getTemperatureAndHumidity()).temp;
        const humidity = (yield getTemperatureAndHumidity()).humidity;
        namespace.addVariable({
            componentOf: device,
            browseName: "temperature",
            dataType: "String",
            value: {
                get: () => new node_opcua_1.Variant({ dataType: node_opcua_1.DataType.String, value: temperature })
            }
        });
        namespace.addVariable({
            componentOf: device,
            browseName: "humidity",
            dataType: "String",
            value: {
                get: () => new node_opcua_1.Variant({ dataType: node_opcua_1.DataType.String, value: humidity })
            }
        });
        yield server.start();
        console.log("Server is now listening ... ( press CTRL+C to stop) ");
        yield new Promise((resolve) => process.once("SIGINT", resolve));
        yield server.shutdown();
    });
}
handleOPCUAServer();
function getTemperatureAndHumidity() {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            // const res = await sensor.read(22, 4);
            const res = { temperature: 50, humidity: 60 };
            return {
                temp: `${res.temperature.toFixed(1)}°C`,
                humidity: `${res.humidity.toFixed(1)}%`
            };
        }
        catch (err) {
            console.error("Failed to read sensor data:", err);
            return {
                temp: `-0°C`,
                humidity: `-0%`
            };
        }
    });
}
//# sourceMappingURL=app.js.map