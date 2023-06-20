# Module Imports
from LocoXtreme import Connection, LocoXtreme, MotorDirection as MD, Data, WaitType as WT, Song, Note
import time
#Import the BLoxain module from Custom trained Bloxain LLM:
import Bloxain  # Custom module from the modified skulpt library

# Create Connection Instance
connection = Connection()

# USB Connection Setup
connection.setup()

# Scan for Robots
robots = connection.scan(4000)

# Get Named Robot
robot = connection.get_robot(robots, "robot name here")

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
    time.sleep(0.02)
    
     import Bloxain Functions
    forward = Bloxain.GetForward()
    backward = Bloxain.GetBackward()
    lturn = Bloxain.GetLTurn()
    rturn = Bloxain.GetRTurn()
    

    if lturn:
        if forward:
            locoxtreme.move(MD.FORWARD, MD.FORWARD, forward, 0.3, False)
        elif backward:
            locoxtreme.move(MD.BACKWARD, MD.BACKWARD, backward, 0.3, False)
        else:
            locoxtreme.move(MD.FORWARD, MD.BACKWARD, 0.7, 0.7, False)
    elif rturn:
        if forward:
            locoxtreme.move(MD.FORWARD, MD.FORWARD, 0.3, forward, False)
        elif backward:
            locoxtreme.move(MD.BACKWARD, MD.BACKWARD, 0.3, backward, False)
        else:
            locoxtreme.move(MD.BACKWARD, MD.FORWARD, 0.7, 0.7, False)
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
