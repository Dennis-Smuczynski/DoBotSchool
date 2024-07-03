import DobotDllType as dType
from colorScanner.videoRead import capture_rgb

def connect_dobot():
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
        return "moved arm to color space",scan_color_move_arm(api)
    else:
        return "error no connection","error"
    
def scan_color_move_arm (api):
    
        # Set command timeout
        dType.SetCmdTimeout(api, 3000)

        # Clear all commands
        dType.ClearAllAlarmsState(api)

        # Set the Dobot to the initial position
        dType.SetPTPJointParams(api, 100, 100, 100, 100, 100, 100, 100, 100)
        dType.SetPTPCommonParams(api, 100, 100)
        dType.SetPTPCoordinateParams(api, 200, 200, 200, 200)

        r, g, b, color_name = capture_rgb()
        print(f"Captured RGB: ({r}, {g}, {b}) - Color name: {color_name}")
        dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 200, 0, 0, 0, 1)
        print("grabbed block")
        
        # Use the captured RGB values (example: move to a position based on color)
        match color_name:
            case "red":
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, 50, 0, 0, 1)   
            case "blue":
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, 100, 0, 0, 1)
            case "green":
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, 150, 0, 0, 1)
            case "yellow":
                dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, 200, 0, 0, 1)
                
        # Always disconnect after operations
        dType.DisconnectDobot(api)
        return color_name
