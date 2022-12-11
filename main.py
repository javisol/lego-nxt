import nxt.locator
import nxt.motor
from multiprocessing import Process

from motor.motor import Motor, MOTOR_PORTS


def move(brick, left_speed, right_speed, left_rotation, right_rotation):
    right_motor = Motor(nxt.motor.Port.B, brick)
    left_motor = Motor(nxt.motor.Port.C, brick)
    p1 = Process(target=left_motor.move, args=(left_speed, left_rotation))
    p2 = Process(target=right_motor.move, args=(right_speed, right_rotation))
    p1.start()
    p2.start()
    p1.join()
    p2.join() 



if __name__ == '__main__':
    brick = nxt.locator.find()
    move(brick, 25, 25, 360, 360)
