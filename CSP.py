import socket

HOST = 'izani.synology.me'
PORT = 8443

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:  # Create a socket
    try:
        sock.connect((HOST, PORT))  # Connect to the server

        student_id = input("Enter the Student ID: ")  # Prompt for student ID
        sock.sendall(student_id.encode())  # Send student ID to server

        response = sock.recv(1024).decode()  # Receive response from server
        print(response)  # Print the full response

        url = response.split(" ")[1]  # Extract URL (assuming format)

    except Exception as e:
        print("Error occurred:", e)  # Handle any exceptions

