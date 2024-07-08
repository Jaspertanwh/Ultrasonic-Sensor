import smbus2
import time

# Define I2C address of the ultrasonic sensor
I2C_ADDRESS = 0x57  # Replace with your sensor's I2C address

def read_distance():
    # Send command to start measurement
    bus.write_byte(I2C_ADDRESS, 0x01)
    time.sleep(0.05)  # Wait for measurement to be taken
    
    # Read 3 bytes from the sensor
    data = bus.read_i2c_block_data(I2C_ADDRESS, 0, 3)
    
    # Combine the bytes to get the distance in millimeters
    distance = (data[0] << 16 | data[1] << 8 | data[2]) / 1000.0
    
    return distance

try:
    # Create an I2C bus instance
    bus = smbus2.SMBus(1)  # 1 indicates /dev/i2c-1, for Raspberry Pi 3/4/Zero
    
    while True:
        # Read distance from sensor
        distance = read_distance()
        cm = distance/10
        
        # if cm>=100 :
        #     m = cm/100
        #     print(f"Distance: {m} m")
        # else:
        # Print the distance
        print(f"Distance: {cm} cm")
        
        # Wait before reading again
        time.sleep(1.0)

except KeyboardInterrupt:
    print("Measurement stopped by user")

finally:
    # Clean up GPIO and I2C connections
    bus.close()
