from machine import Pin, ADC, time_pulse_us

# Pin for QRE1113 sensorens analoge output
qre_pin = ADC(Pin(26))  # GP26 (ADC0)
DARK_THRESHOLD = 57000   # Tærskelværdi for reflektionssensoren

pwm_pin = Pin(28, Pin.IN)  # Pin til afstandssensor

def read_distance_cm():
    pulse_duration = time_pulse_us(pwm_pin, 1)
    if pulse_duration > 0:
        distance_cm = pulse_duration / 100  # Konverterer pulsvarigheden direkte til cm
        return distance_cm
    else:
        return None

def is_over_dark_surface():
    """
    Læser QRE1113 infrarøde refleksionssensor.
    Returnerer True, hvis den er over en mørk overflade, ellers False.
    """
    analog_value = qre_pin.read_u16()  # Læs det analoge signal
    print(f"Analog værdi: {analog_value}")  # Udskriv den aflæste værdi
    return analog_value < DARK_THRESHOLD  # Returner True, hvis signalet er under tærskelværdien
