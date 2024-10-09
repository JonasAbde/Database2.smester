# motor.py
from machine import Pin, PWM

# Definer pins for venstre motor
left_in1 = Pin(16, Pin.OUT)
left_in2 = Pin(17, Pin.OUT)
left_ena = PWM(Pin(20))
left_ena.freq(1000)

# Definer pins for højre motor
right_in1 = Pin(18, Pin.OUT)
right_in2 = Pin(19, Pin.OUT)
right_enb = PWM(Pin(21))
right_enb.freq(1000)

def move_forward_pwm(left_pwm_value, right_pwm_value):
    # Sæt retning til fremad
    left_in1.high()
    left_in2.low()
    right_in1.high()
    right_in2.low()
    # Sæt PWM-værdier
    left_ena.duty_u16(int(left_pwm_value))
    right_enb.duty_u16(int(right_pwm_value))

def stop():
    # Stop motorerne
    left_in1.low()
    left_in2.low()
    right_in1.low()
    right_in2.low()
    left_ena.duty_u16(0)
    right_enb.duty_u16(0)
