import socket
import threading

def handle_client(client_socket, username):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received from {username}: {data}")

        if data == "#" or data == "Exit":
            break

        reply = input(f"Reply to {username}: ")
        client_socket.send(reply.encode('utf-8'))

        if reply == "#" or reply == "Exit":
            break

    client_socket.close()
    print(f"Connection with {username} closed")

def main():
    host = '0.0.0.0'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)  # Listen for up to 2 connections

    print(f"Waiting for connections on port {port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        username = input("Enter username: ")

        client_handler = threading.Thread(target=handle_client, args=(client_socket, username))
        client_handler.start()

if __name__ == "__main__":
    main()
