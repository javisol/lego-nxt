import nxt.locator
import nxt.motor

MOTOR_PORTS = {
    "LEFT": "nxt.motor.Port.B",
    "RIGHT": "nxt.motor.Port.C",
    "FRONT": "nxt.motor.Port.A",
    }

class Motor:
    def __init__(self, motor_port, brick):
        self.motor_port  = motor_port
        self.brick = brick
        self.motor = brick.get_motor(motor_port)

    def move(self, speed:int = 25, rotation:int = 360):
            self.motor.turn(speed, rotation) # full circle

    #TODO: check protocol problems
    def brake(self):
        self.motor.brake()
