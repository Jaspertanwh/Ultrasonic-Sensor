import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the trigger, echo, and alert
TRIG = 23
ECHO = 24
ALERT = 17

# Set up the GPIO pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(ALERT, GPIO.OUT)

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

        # Check if the distance is less than 150 cm and trigger ALERT pin
        if dist < 150:
            GPIO.output(ALERT, True)
        else:
            GPIO.output(ALERT, False)

        time.sleep(1)  # Wait for 1 second before the next measurement

except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
