import socket
import threading

def handle_client(client_socket, username):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(f"Received from {username}: {message}")

        if message == "#":
            break

        reply = input(f"Reply to {username}: ")
        client_socket.send(reply.encode('utf-8'))

        if reply == "#":
            break

    client_socket.close()
    print(f"Connection with {username} closed")

def main():
    host = '0.0.0.0'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Waiting for connections on port {port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        # Start a new thread to handle the communication with the connected client
        client_thread = threading.Thread(target=handle_client, args=(conn, f"User{addr}"))
        client_thread.start()

if __name__ == "__main__":
    main()
