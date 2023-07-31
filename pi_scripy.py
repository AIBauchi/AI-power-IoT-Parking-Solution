#importing the library 
import RPi.GPIO as GPIO
import cv2
import pickle
import socket
from gpiozero import Servo
from time import sleep

# Initialize the servo motor on GPIO pin 25
servo = Servo(25)

# Define the GPIO pin for the IR sensor
sensor = 16

# Set up GPIO mode and input for the IR sensor
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN)

def send_frame():
    """Capture and send a compressed frame to the PC for processing.

    Returns:
        str: The response from the PC as a string.
    """
    # Set up the socket for communication
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8000))  # Use the IP of your Raspberry Pi
    server_socket.listen(1)

    try:
        # Accept incoming connection from PC
        connection, client_address = server_socket.accept()
        
        # Start capturing video from the camera
        camera = cv2.VideoCapture(0)  # Use the correct camera index if multiple cameras are connected

        try:
            while True:
                # Capture frame from the camera
                ret, frame = camera.read()
                if not ret:
                    break

                # Compress the frame using JPEG encoding with a quality of 70 (adjust as needed)
                _, compressed_frame = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 70])

                # Serialize the compressed frame
                data = pickle.dumps(compressed_frame)

                # Send the frame over the network
                connection.sendall(data)

                # Wait for the response from the client (PC)
                response = connection.recv(4096)

                # Process the response (you can do whatever you want with it)
                if response:
                    return response.decode()

        finally:
            # Release the camera and close the connection
            camera.release()
    except Exception as e:
        print("Error:", e)
    finally:
        connection.close()
        server_socket.close()

try:
    # Initialize the flag to track IR sensor activity
    is_sensor_active = False

    while True:
        # Check if the IR sensor detects an obstacle (car)
        if GPIO.input(sensor):
            if not is_sensor_active:
                # The sensor is active, set the flag and send the frame to the PC for processing
                is_sensor_active = True
                response = send_frame()

                # If the response from the PC is True, open the gate using the servo motor
                if response == "True":
                    servo.min()
                    sleep(2)
                    servo.max()
        else:
            # No obstacle detected by the IR sensor, reset the flag and close the gate
            if is_sensor_active:
                is_sensor_active = False
                servo.max()

except KeyboardInterrupt:
    # Clean up GPIO pins on keyboard interrupt
    GPIO.cleanup()
