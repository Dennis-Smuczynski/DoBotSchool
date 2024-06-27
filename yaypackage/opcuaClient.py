from opcua import Client
import time

def get_climate_data():
    # URL of the OPC UA server
    url = "opc.tcp://localhost:4334/UA/MyLittleServer"

    # Create a client instance
    client = Client(url)

    try:
        # Connect to the server
        client.connect()
        print("Connected to OPC UA Server")

        # Get the root node
        root = client.get_root_node()

        # Print root node
        print(f"Root node: {root}")

        # Browse the objects folder
        objects = client.get_objects_node()
        print(f"Objects node: {objects}")


        # # Print all child nodes of the objects node
        # print("Children of Objects node:")
        # for child in objects.get_children():
        #     print(f"Child: {child} - BrowseName: {child.get_browse_name()}")
        # Get the ClimateSensor object
        climate_sensor = objects.get_child(["1:ClimateSensor"])
        print(f"ClimateSensor node: {climate_sensor}")

        # for child in objects.get_children():
        #     print(f"Child: {child} - BrowseName: {child.get_browse_name()}")

        # Get the temperature and humidity variables
        temperature_var = climate_sensor.get_child(["1:temperature"])
        humidity_var = climate_sensor.get_child(["1:humidity"])

        # Read the values
        temperature = temperature_var.get_value()
        humidity = humidity_var.get_value()

        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")

    finally:
        # Close the client connection
        client.disconnect()
        print("Disconnected from OPC UA Server")
    return temperature, humidity 