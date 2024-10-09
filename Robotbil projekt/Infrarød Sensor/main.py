import sensor
import motor
import time

DESIRED_DISTANCE = 50  # Ønsket afstand til væggen i cm
BASE_PWM = 17000       # Grundlæggende PWM-værdi
ADJUSTMENT = 10000      # Justeringsværdi for højre PWM
ADJUSTMENT1 = 9000     # Justeringsværdi for venstre PWM
SLOW_RIGHT_PWM = 10000 # PWM-værdi for langsom kørsel til højre

while True:
    distance = sensor.read_distance_cm()

    if distance is not None:
        print(f"Aflæst afstand: {distance:.2f} cm")
        error = DESIRED_DISTANCE - distance

        # Tjek refleksionssensoren
        if sensor.is_over_dark_surface():  # Hvis sensoren er over en mørk overflade
            motor.move_forward_pwm(BASE_PWM, SLOW_RIGHT_PWM)  # Kør venstre motor normalt, højre motor langsomt
            print("Over mørk overflade: Kører venstre")
        elif error > 0:
            # For tæt på væggen, stop højre motor for at rette op
            motor.move_forward_pwm(BASE_PWM, 0)  # Stop højre motor
            print("For tæt: Stopper højre motor for at rette op")
        elif error < 0:
            # For langt fra væggen, øg højre motors PWM en smule
            motor.move_forward_pwm(BASE_PWM, BASE_PWM + ADJUSTMENT1)
            print("For langt: Øger højre motors PWM en smule")
        else:
            # På ønsket afstand, kør ligeud
            motor.move_forward_pwm(BASE_PWM, BASE_PWM)
            print("På ønsket afstand: Kører ligeud")
    else:
        # Ingen afstandsmåling, stop motorerne
        motor.stop()
        print("Ingen afstandsmåling modtaget. Stopper motorerne.")

    time.sleep(0.01)
