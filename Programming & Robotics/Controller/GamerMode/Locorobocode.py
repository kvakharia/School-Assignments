# Module Imports
from LocoXtreme import Connection, LocoXtreme, MotorDirection as MD, Data, WaitType as WT, Song, Note
import time
import Bloxain
print('Imported Custom Library! Loading...')


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
    
   
    lturn = Bloxain.GetForward()
    rturn = Bloxain.GetBackward()
    forward = Bloxain.GetLTurn()
    backward = Bloxain.GetRTurn()
    
    
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
