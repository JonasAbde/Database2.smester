# Filename: controller.py

import pygame
import socket
import time

# Initialize pygame to use the Xbox controller
pygame.init()
pygame.joystick.init()

# Check if the Xbox controller is connected
if pygame.joystick.get_count() == 0:
    print("No Xbox controller found.")
    exit()

# Connect the Xbox controller
controller = pygame.joystick.Joystick(0)
controller.init()

print("Xbox controller connected via Bluetooth.")

# IP address of your Raspberry Pi Pico W
PICO_IP = '192.168.1.45'  # Update this with the correct IP address of your Pico W
UDP_PORT = 5005  # Same port as the UDP server on Pico W

# Create a UDP client socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Function to send commands via UDP with speeds for both motors
def send_command(command, speed_left, speed_right):
    try:
        message = f"{command}:{speed_left}:{speed_right}"  # Send command + speeds for left and right motors
        s.sendto(message.encode('utf-8'), (PICO_IP, UDP_PORT))
        print(f"Sent: {message} to {PICO_IP}:{UDP_PORT}")
    except Exception as e:
        print(f"Error sending command: {e}")

boost_active = False  # Variable to keep track of whether boost is active
normal_speed = 70  # Adjust normal speed percentage if needed
boost_speed = 100  # Boost speed set to maximum PWM percentage

# Controller event-handling loop
while True:
    # Check for events (controller input)
    pygame.event.pump()

    # Read D-pad (hat) position for forward/backward and turning
    dpad_x, dpad_y = controller.get_hat(0)  # Get D-pad position

    # Check if the A button (boost) is pressed
    button_a = controller.get_button(0)

    # Adjust speed based on boost status
    current_speed = boost_speed if boost_active else normal_speed

    # If A button is pressed, activate boost; else, deactivate it
    if button_a and not boost_active:
        send_command('BOOST_ON', current_speed, current_speed)
        boost_active = True
    elif not button_a and boost_active:
        send_command('BOOST_OFF', current_speed, current_speed)
        boost_active = False

    # Variables to adjust left and right motor speeds
    speed_left = 0
    speed_right = 0

    # Combined movement forward/backward and turning based on D-pad
    if dpad_y == 1:  # Up arrow (forward)
        speed_left = current_speed
        speed_right = current_speed
    elif dpad_y == -1:  # Down arrow (backward)
        speed_left = -current_speed
        speed_right = -current_speed

    # Adjust for turning (combine with forward/backward movement)
    if dpad_x == -1:  # Left arrow (turn left)
        speed_right *= 0.6  # Reduce speed of right motor to turn left
    elif dpad_x == 1:  # Right arrow (turn right)
        speed_left *= 0.6  # Reduce speed of left motor to turn right

    # If both X and Y are zero (no input), stop the motors
    if dpad_x == 0 and dpad_y == 0:
        send_command('STOP', 0, 0)
    else:
        # Send the movement command
        send_command('MOVE', speed_left, speed_right)

    # Debug print for D-pad status
    print(f'D-pad position (X): {dpad_x}, (Y): {dpad_y}, Left speed = {speed_left}, Right speed = {speed_right}, Boost: {boost_active}')

    # Reduce sleep delay to increase responsiveness
    time.sleep(0.02)  # Reduced from 0.1 to 0.02 seconds
