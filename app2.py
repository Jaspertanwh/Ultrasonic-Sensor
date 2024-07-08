# from gpiozero import DistanceSensor
# from gpiozero.pins.pigpio import PiGPIOFactory
# from time import sleep

# # Use pigpio pin factory
# factory = PiGPIOFactory()

# # Create DistanceSensor instance with the pigpio pin factory
# sensor = DistanceSensor(echo=24, trigger=23, pin_factory=factory)

# while True:
#     try:
#         distance = sensor.distance
#         print(f"{distance:.2f} m")
#     except Exception as e:
#         print(f"Error: {e}")
#     sleep(5)


import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the trigger and echo
TRIG = 23
ECHO = 24

# Set up the GPIO pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    # Send a 10us pulse to trigger
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Wait for the echo to start
    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    # Wait for the echo to stop
    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    # Calculate the duration of the echo pulse
    duration = end_time - start_time

    # Calculate the distance
    distance = (duration * 34300) / 2  # Speed of sound in cm/s

    return distance

try:
    while True:
        dist = get_distance()
        print(f"Distance: {dist:.2f} cm")
        time.sleep(1)  # Wait for 1 second before the next measurement
except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
