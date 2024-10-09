# main.py
import sensor
import motor
import time

# Constants
BASE_SPEED = 20000
TURN_SPEED = 15000
PUSH_DURATION = 3  # Duration to push the object (seconds)
RETURN_DURATION = 3  # Duration to return (seconds)
OBJECT_DETECTION_DISTANCE = 50  # Detection threshold (cm)


def rotate_in_circle():
    # Rotate the robot in a circle
    motor.turn_left(speed=TURN_SPEED)


def move_towards_object():
    # Move forward to push the object
    start_time = time.time()
    motor.move_forward()
    while time.time() - start_time < PUSH_DURATION:
        if sensor.is_black_line_detected():
            motor.stop()
            print("Black line detected! Stopping.")
            return True  # Detected black line
        time.sleep(0.01)
    motor.stop()
    return False  # Did not detect black line


def return_to_start():
    # Move backward to return to the starting position
    motor.move_backward()
    time.sleep(RETURN_DURATION)
    motor.stop()


def main():
    while True:
        # Step 1: Rotate in a circle
        rotate_in_circle()

        # Step 2: Check for object detection
        distance = sensor.read_distance_cm()
        if distance is not None and distance < OBJECT_DETECTION_DISTANCE:
            print(f"Object detected at {distance:.2f} cm")
            motor.stop()
            time.sleep(0.5)

            # Step 3: Turn towards the object
            # Assuming the robot is already facing the object after stopping rotation
            # If not, implement a function to align with the object

            # Step 4: Move forward to push the object
            black_line_detected = move_towards_object()

            # Step 5: Return to starting position if black line was not detected
            if not black_line_detected:
                return_to_start()

            # Step 6: Resume rotating in a circle
            print("Resuming rotation.")
            continue

        time.sleep(0.1)  # Small delay to prevent CPU overload


if __name__ == "__main__":
    main()
