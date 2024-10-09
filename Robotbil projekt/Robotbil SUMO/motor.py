# motor.py
from machine import Pin, PWM

# Define pins for the left motor
left_in1 = Pin(16, Pin.OUT)
left_in2 = Pin(17, Pin.OUT)
left_ena = PWM(Pin(20))
left_ena.freq(1000)

# Define pins for the right motor
right_in1 = Pin(18, Pin.OUT)
right_in2 = Pin(19, Pin.OUT)
right_enb = PWM(Pin(21))
right_enb.freq(1000)

def move_forward(left_speed=20000, right_speed=20000):
    # Set direction to forward
    left_in1.high()
    left_in2.low()
    right_in1.high()
    right_in2.low()
    # Set PWM duty cycles
    left_ena.duty_u16(int(left_speed))
    right_enb.duty_u16(int(right_speed))

def move_backward(left_speed=20000, right_speed=20000):
    # Set direction to backward
    left_in1.low()
    left_in2.high()
    right_in1.low()
    right_in2.high()
    # Set PWM duty cycles
    left_ena.duty_u16(int(left_speed))
    right_enb.duty_u16(int(right_speed))

def turn_left(speed=20000):
    # Left motor backward, right motor forward
    left_in1.low()
    left_in2.high()
    right_in1.high()
    right_in2.low()
    # Set PWM duty cycles
    left_ena.duty_u16(int(speed))
    right_enb.duty_u16(int(speed))

def turn_right(speed=20000):
    # Left motor forward, right motor backward
    left_in1.high()
    left_in2.low()
    right_in1.low()
    right_in2.high()
    # Set PWM duty cycles
    left_ena.duty_u16(int(speed))
    right_enb.duty_u16(int(speed))

def stop():
    # Stop the motors
    left_in1.low()
    left_in2.low()
    right_in1.low()
    right_in2.low()
    left_ena.duty_u16(0)
    right_enb.duty_u16(0)
