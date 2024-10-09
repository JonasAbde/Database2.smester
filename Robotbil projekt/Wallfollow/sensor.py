from machine import Pin, time_pulse_us

pwm_pin = Pin(28, Pin.IN)

def read_distance_cm():
    pulse_duration = time_pulse_us(pwm_pin, 1)
    if pulse_duration > 0:
        distance_cm = pulse_duration / 100  # Konverterer pulsvarigheden direkte til cm
        return distance_cm
    else:
        return None

