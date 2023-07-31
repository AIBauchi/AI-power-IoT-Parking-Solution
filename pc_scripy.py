import cv2
import pickle
import socket
import torch

PATH = "path/to/model"


model = torch.load(PATH)
model.eval()

def receive_frame():
    """Receive a compressed frame from the Raspberry Pi, process it with the OCR model, and send a response back.

    The response should be a boolean string ('True' or 'False') representing whether the license plate is in the database.
    """

    # Set up the socket to connect to the Raspberry Pi
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('raspberry_pi_ip', 8000))  # Replace 'raspberry_pi_ip' with the IP of your Raspberry Pi

    try:
        # Receive the serialized frame from the Raspberry Pi
        data = b''
        while True:
            packet = client_socket.recv(4096)
            if not packet:
                break
            data += packet

        # Deserialize the frame
        frame = pickle.loads(data)

        #send frame to model
        recognized_text = ocr_process(frame)

        # Perform database lookup (assuming 'database_lookup' is a function that checks if the license plate exists in the database)
        if database_lookup(recognized_text):
            response = "True"
        else:
            response = "False"

        # Send the response back to the Raspberry Pi
        client_socket.sendall(response.encode())

    finally:
        cv2.destroyAllWindows()
        client_socket.close()

def ocr_process(frame):
    """Process the frame using the OCR model and return the recognized text."""
    recognized_text = model.predict(frame)
    # recognized_text = "ABC123"
    return recognized_text

def database_lookup(recognized_text):
    """Perform a database lookup to check if the recognized text exists in the database."""
    with open("data.txt", "r") as file:
        data = file.read()
    if recognized_text in data:
        return True
    else:
        return False

if __name__ == "__main__":
    receive_frame()
