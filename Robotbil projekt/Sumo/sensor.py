# sensor.py
from machine import Pin, time_pulse_us
import time

# Ultrasonic sensor pins
trigger_pin = Pin(27, Pin.OUT)
echo_pin = Pin(28, Pin.IN)

# Infrared sensor pin
ir_pin = Pin(22, Pin.IN)  # Adjust pin number as needed

def read_distance_cm():
    # Send a 10us pulse to trigger the ultrasonic sensor
    trigger_pin.low()
    time.sleep_us(2)
    trigger_pin.high()
    time.sleep_us(10)
    trigger_pin.low()

    # Measure the pulse duration on the echo pin
    pulse_duration = time_pulse_us(echo_pin, 1, 30000)  # Timeout after 30ms

    if pulse_duration > 0:
        # Calculate distance (pulse duration in microseconds)
        distance_cm = (pulse_duration / 2) / 29.1  # Speed of sound: 343 m/s
        return distance_cm
    else:
        return None

def is_black_line_detected():
    # Returns True if the infrared sensor detects a black line
    return ir_pin.value() == 0  # Adjust based on your sensor's output logic
