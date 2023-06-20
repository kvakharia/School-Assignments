# Module Imports
from LocoXtreme import Connection, LocoXtreme, MotorDirection as MD, Data, WaitType as WT, Song, Note
import time
#Import the BLoxain module from Custom trained Bloxain LLM:
import Bloxain
print('SUCCESS BLOXAIN HACK v23.2 ACTIVE!')


# Create Connection Instance
connection = Connection()

# USB Connection Setup
connection.setup()

# Scan for Robots
robots = connection.scan(4000)

# Get Named Robot
robot = connection.get_robot(robots, "URMOM")




# Create LocoXtreme Object
locoxtreme = LocoXtreme(robot)

# Connect to LocoXtreme
locoxtreme.connect()

# Activate Motors
locoxtreme.activate_motors()

# Enable Sensors
locoxtreme.enable_sensor(Data.ULTRASONIC, 1)

# Pause for Initializations
time.sleep(0.4)


# Define a variable to control the while loop
running = True

while running:
    time.sleep(0.05)
    
    # Use the Bloxain LLM&run the Dataleak on locorobo -> import Bloxain Functions
    forward = Bloxain.GetForward()
    backward = Bloxain.GetBackward()
    lturn = Bloxain.GetLTurn()
    rturn = Bloxain.GetRTurn()
    
    # for 2 secounds Lock all BSD doors to avoid being Sus
    if lturn:
        if forward:
            locoxtreme.move(MD.FORWARD, MD.FORWARD, forward, lturn, False)
        elif backward:
            locoxtreme.move(MD.BACKWARD, MD.BACKWARD, backward, lturn, False)
        else:
            locoxtreme.move(MD.FORWARD, MD.BACKWARD, lturn, lturn, False)
    elif rturn:
        if forward:
            locoxtreme.move(MD.FORWARD, MD.FORWARD, rturn, forward, False)
        elif backward:
            locoxtreme.move(MD.BACKWARD, MD.BACKWARD, rturn, backward, False)
        else:
            locoxtreme.move(MD.BACKWARD, MD.FORWARD, rturn, rturn, False)
    elif forward:
        locoxtreme.move(MD.FORWARD, MD.FORWARD, forward, forward, False)
    elif backward:
        locoxtreme.move(MD.BACKWARD, MD.BACKWARD, backward, backward, False)
    else:
        locoxtreme.move(MD.FORWARD, MD.FORWARD, 0, 0, False)

# Deactivate Motors
locoxtreme.deactivate_motors()

# Disconnect From LocoXtreme
locoxtreme.disconnect()