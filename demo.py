import cv2
import pickle
import socket

def send_frame():
    # Set up the socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8000))  # Use the IP of your Raspberry Pi
    server_socket.listen(1)

    # Start capturing video
    camera = cv2.VideoCapture(0)  # Use the correct camera index if multiple cameras are connected

    try:
        # Capture frame
        ret, frame = camera.read()

        # Serialize the frame
        data = pickle.dumps(frame)

        # Send the frame over the network
        connection, client_address = server_socket.accept()
        connection.sendall(data)
        connection.close()

    finally:
        camera.release()
        server_socket.close()

if __name__ == "__main__":
    send_frame()
