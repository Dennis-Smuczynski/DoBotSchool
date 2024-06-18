from .dobotDllType import *
from .videoRead import capture_rgb

def connect_dobot():
    # Load Dll
    api = load()

    # Connect Dobot
    CON_STR = {
        DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
        DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
        DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"
    }

    # Replace 'COM3' with the appropriate port for your system
    state = ConnectDobot(api, "COM9", 115200)[0]

    print("Connect status:", CON_STR[state])
    if state == DobotConnect.DobotConnect_NoError:
        return "moved arm to color space",scan_color_move_arm(api)
    else:
        return "error no connection","error"
    
def scan_color_move_arm (api):
    
        # Set command timeout
        SetCmdTimeout(api, 3000)

        # Clear all commands
        ClearAllAlarmsState(api)

        # Set the Dobot to the initial position
        SetPTPJointParams(api, 100, 100, 100, 100, 100, 100, 100, 100)
        SetPTPCommonParams(api, 100, 100)
        SetPTPCoordinateParams(api, 200, 200, 200, 200)

        r, g, b, color_name = capture_rgb()
        print(f"Captured RGB: ({r}, {g}, {b}) - Color name: {color_name}")
        SetPTPCmd(api, PTPMode.PTPMOVLXYZMode, 200, 0, 0, 0, 1)
        print("grabbed block")
        
        # Use the captured RGB values (example: move to a position based on color)
        match color_name:
            case "red":
                SetPTPCmd(api, PTPMode.PTPMOVLXYZMode, 250, 50, 0, 0, 1)   
            case "blue":
                SetPTPCmd(api, PTPMode.PTPMOVLXYZMode, 250, 100, 0, 0, 1)
            case "green":
                SetPTPCmd(api, PTPMode.PTPMOVLXYZMode, 250, 150, 0, 0, 1)
            case "yellow":
                SetPTPCmd(api, PTPMode.PTPMOVLXYZMode, 250, 200, 0, 0, 1)
                
        # Always disconnect after operations
        DisconnectDobot(api)
        return color_name
