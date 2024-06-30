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

    # Replace 'COM' with the appropriate port for your system
    state = ConnectDobot(api, "COM9", 115200)[0]

    print("Connect status:", CON_STR[state])
    if state == DobotConnect.DobotConnect_NoError:
        return "starting process...",scan_color_move_arm(api)
    else:
        return "error no connection","error"
    
def scan_color_move_arm (api):
    
    # Set command timeout
    SetCmdTimeout(api, 3000)

    # Clear all commands
    ClearAllAlarmsState(api)

    armMoveToStart(api)
    
    r, g, b, color = armPickAndMoveToSensor(api)
    
    armMoveToColorSpot(api,color)
              
    # Always disconnect after operations
    DisconnectDobot(api)
    
    return color
    

def turnOnSuction(api):
    SetEndEffectorSuctionCup( api, True, True, isQueued = 0)

def turnOffSuction(api):
    SetEndEffectorSuctionCup(api, True, False, isQueued = 0)

def moveArmXYZR(api,x,y,z,r):
    SetPTPCmd(api, PTPMode.PTPMOVLXYZMode, x, y, z, r)[0]
        
def getColor():
    return capture_rgb()
        
def armMoveToStart(api):
    moveArmXYZR(api,200,-50,-58,0)

def armPickAndMoveToSensor(api):
        turnOnSuction(api)
        moveArmXYZR(api,250,-50,-58,0)
        return getColor()
    
def armMoveToColorSpot(api,color_name):
    match color_name:
        case "red":
            moveArmXYZR(api,250,-40,0,0) 
        case "blue":
            moveArmXYZR(api,250,-30,0,0) 
        case "green":
            moveArmXYZR(api,250,-20,0,0) 
        case "yellow":
            moveArmXYZR(api,250,-10,0,0) 

