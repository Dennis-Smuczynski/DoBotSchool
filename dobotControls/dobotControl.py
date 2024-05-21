import DobotDllType as dType

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
    
    if state == dType.DobotConnect.DobotConnect_NoError:
        # Move to position (x=250, y=0, z=0, r=0)
        dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, 250, 0, 0, 0, 1)
        print("Moved to position (250, 0, 0)")

# Always disconnect after operations
dType.DisconnectDobot(api)
