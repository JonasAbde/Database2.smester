import sensor
import motor
import time

DESIRED_DISTANCE = 50 # Ønsket afstand til væggen i cm
BASE_PWM = 20000       # Grundlæggende PWM-værdi
ADJUSTMENT = 7000      # Justeringsværdi for højre PWM
ADJUSTMENT1 = 6000     # Justeringsværdi for venstre PWM

while True:
    distance = sensor.read_distance_cm()

    if distance is not None:
        print(f"Aflæst afstand: {distance:.2f} cm")
        error = DESIRED_DISTANCE - distance

        if error > 0:
            # For tæt på væggen, øg venstre motors PWM en smule
            motor.move_forward_pwm(BASE_PWM + ADJUSTMENT, BASE_PWM)
            print("For tæt: Øger venstre motors PWM en smule")
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

    time.sleep(0.05)