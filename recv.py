import cv2
import pickle
import socket

def receive_frame():
    # Set up the socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('0.0.0.0', 8000))  # Replace '0.0.0.0' with the IP of your Raspberry Pi

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

        # Now you have the frame as a regular OpenCV image
        # You can do whatever you want with it
        # For example, display the frame
        cv2.imshow('Received Frame', frame)
        cv2.waitKey(0)  # Wait until a key is pressed to close the window

    finally:
        cv2.destroyAllWindows()
        client_socket.close()

if __name__ == "__main__":
    receive_frame()
