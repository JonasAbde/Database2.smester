from machine import Pin, PWM

# Definer pins for venstre og højre motor
left_in1 = Pin(16, Pin.OUT)
left_in2 = Pin(17, Pin.OUT)
left_ena = PWM(Pin(20))  # PWM til venstre motor hastighed (ENA)
left_ena.freq(1000)

right_in1 = Pin(18, Pin.OUT)
right_in2 = Pin(19, Pin.OUT)
right_enb = PWM(Pin(21))  # PWM til højre motor hastighed (ENB)
right_enb.freq(1000)


def set_speed_left(speed):
    """Indstil hastigheden for venstre motor."""
    speed = max(0, min(100, speed))
    duty = int(speed * 65535 / 100)
    left_ena.duty_u16(duty)


def set_speed_right(speed):
    """Indstil hastigheden for højre motor."""
    speed = max(0, min(100, speed))
    duty = int(speed * 65535 / 100)
    right_enb.duty_u16(duty)


def move(speed_left, speed_right):
    """Bevæg begge motorer med separate hastigheder."""
    if speed_left > 0:
        left_in1.high()
        left_in2.low()
    else:
        left_in1.low()
        left_in2.high()

    if speed_right > 0:
        right_in1.high()
        right_in2.low()
    else:
        right_in1.low()
        right_in2.high()

    set_speed_left(abs(speed_left))
    set_speed_right(abs(speed_right))


def stop():
    """Stop begge motorer."""
    left_in1.low()
    left_in2.low()
    right_in1.low()
    right_in2.low()
    set_speed_left(0)
    set_speed_right(0)
