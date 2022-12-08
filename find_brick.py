import time
import nxt.locator
import nxt.motor
import nxt.sensor
import nxt.sensor.generic
from nxt.sensor import Type


def motor():
    with nxt.locator.find() as b:
        print("Found brick:", b.get_device_info()[0])
        motor_right = b.get_motor(nxt.motor.Port.B)
        motor_right.turn(25, 360) # full circle

        motor_left = b.get_motor(nxt.motor.Port.C)
        motor_left.turn(25, 360) # full circle

        motor_front = b.get_motor(nxt.motor.Port.A)
        motor_front.turn(25, 360) # full circle

def ultra_sensor():
    with nxt.locator.find() as b:
        sensor = b.get_sensor(nxt.sensor.Port.S2)
        while True:
            distance_cm = sensor.get_sample()
            print(distance_cm)
            time.sleep(0.5)

def rgb_sensor():
    with nxt.locator.find() as b:
        sensor = b.get_sensor(nxt.sensor.Port.S2, nxt.sensor.generic.Color)
        while True:
            #value = sensor.get_sample()
            #print(value)
            color = sensor.get_light_color()
            print(color)
            print(type(color))
            time.sleep(2)
            sensor.set_light_color(Type.COLOR_GREEN)
            time.sleep(2)
            sensor.set_light_color(Type.COLOR_BLUE)
            time.sleep(2)
            sensor.set_light_color(Type.COLOR_RED)
            time.sleep(2)
            sensor.set_light_color(Type.COLOR_FULL)
            time.sleep(2)
            sensor.set_light_color(Type.COLOR_NONE)
            time.sleep(2)

def light_sensor():
    with nxt.locator.find() as b:
        sensor = b.get_sensor(nxt.sensor.Port.S2, nxt.sensor.generic.Color)
        sensor.set_light_color(Type.COLOR_NONE)
        sensor.set_light_color(Type.COLOR_EXIT)
        time.sleep(2)
        while True:
            value = sensor.get_reflected_light(Type.COLOR_FULL)
            print(value)
            time.sleep(0.5)


def touch_sensor():
    with nxt.locator.find() as b:
        sensor = b.get_sensor(nxt.sensor.Port.S2, nxt.sensor.generic.Touch)
        while True:
            value = sensor.is_pressed()
            print(value)
            time.sleep(0.5)

def touch_analog_sensor():
    '''
    value is nxt.sensor.analog.RawReading
    (<Port.S2: 1>, True, False, <Type.SWITCH: 1>, <Mode.BOOL: 32>, 184, 184, 1, 184)
    port, valid, calibrated, sensor_type, mode, calibrated_value, normalized_value, scaled_value, raw_value)
    '''
    with nxt.locator.find() as b:
        sensor = b.get_sensor(nxt.sensor.Port.S2, nxt.sensor.analog.BaseAnalogSensor)
        while True:
            value = sensor.get_input_values()
            print(value)
            time.sleep(0.5)

def sound():
    with nxt.locator.find() as b:
        b.play_tone(440, 250) # set a volume on brick settings


if __name__ == '__main__':
    #sound()
    #motor()
    #ultra_sensor()
    #rgb_sensor()
    #light_sensor()
    #touch_sensor()
    touch_analog_sensor()

