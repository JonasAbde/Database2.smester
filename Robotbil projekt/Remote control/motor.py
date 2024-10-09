# Filename: motor.py

from machine import Pin, PWM

# Define pins for left and right motors
left_in1 = Pin(16, Pin.OUT)
left_in2 = Pin(17, Pin.OUT)
left_ena = PWM(Pin(20))  # PWM for left motor speed (ENA)
left_ena.freq(2000)  # PWM frequency

right_in1 = Pin(18, Pin.OUT)
right_in2 = Pin(19, Pin.OUT)
right_enb = PWM(Pin(21))  # PWM for right motor speed (ENB)
right_enb.freq(2000)  # PWM frequency

def set_speed_left(speed):
    """Set the speed for the left motor."""
    speed = max(0, min(100, speed))
    duty = int(speed * 65535 / 100)
    left_ena.duty_u16(duty)

def set_speed_right(speed):
    """Set the speed for the right motor."""
    speed = max(0, min(100, speed))
    duty = int(speed * 65535 / 100)
    right_enb.duty_u16(duty)

def move(speed_left, speed_right, cal_left=1.0, cal_right=1.0):
    """Move both motors with separate speeds and calibration."""
    # Apply calibration
    speed_left *= cal_left
    speed_right *= cal_right

    # Ensure speed limits
    speed_left = max(-100, min(100, speed_left))
    speed_right = max(-100, min(100, speed_right))

    # Left motor direction
    if speed_left > 0:
        left_in1.high()
        left_in2.low()
    elif speed_left < 0:
        left_in1.low()
        left_in2.high()
    else:
        left_in1.low()
        left_in2.low()

    # Right motor direction
    if speed_right > 0:
        right_in1.high()
        right_in2.low()
    elif speed_right < 0:
        right_in1.low()
        right_in2.high()
    else:
        right_in1.low()
        right_in2.low()

    set_speed_left(abs(speed_left))
    set_speed_right(abs(speed_right))

def stop():
    """Stop both motors."""
    left_in1.low()
    left_in2.low()
    right_in1.low()
    right_in2.low()
    set_speed_left(0)
    set_speed_right(0)
