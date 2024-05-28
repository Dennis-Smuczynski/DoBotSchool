import DobotDllType as dType
from .videoread import capture_rgb  # Import the capture_rgb function

# Load Dll
api = dType.load()

# Connect Dobot
CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"
}

# Replace 'COM3' with the appropriate port for your system
state = dType.ConnectDobot(api, "COM3", 115200)[0]

print("Connect status:", CON_STR[state])

if state == dType.DobotConnect.DobotConnect_NoError:
    # Set command timeout
    dType.SetCmdTimeout(api, 3000)

    # Clear all commands
    dType.ClearAllAlarmsState(api)

    # Set the Dobot to the initial position
    dType.SetPTPJointParams(api, 100, 100, 100, 100, 100, 100, 100, 100)
    dType.SetPTPCommonParams(api, 100, 100)
    dType.SetPTPCoordinateParams(api, 200, 200, 200, 200)

    # Move to the initial point
    dType.SetPTPJumpParams(api, 20, 200)
    dType.SetPTPJump2Params(api, 20, 200)
    dType.SetPTPCommonParams(api, 100, 100)

    dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 200, 0, 0, 0, 1)
    print("Moved to initial position")

    # Capture RGB values from the camera
    r, g, b, color_name = capture_rgb()
    print(f"Captured RGB: ({r}, {g}, {b}) - Color name: {color_name}")

    # Use the captured RGB values (example: move to a position based on color)
    if color_name == "red":
        dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, 0, 0, 0, 1)
        print("Moved to position (250, 0, 0) based on detected red color")

# Always disconnect after operations
dType.DisconnectDobot(api)
