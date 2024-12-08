import socket   #Imports the Python socket
import threading #Imports the threading module

def handle_client(conn, addr):  #function with a socket connection and the address of client as parameters.
    print(f"Connection established with {addr}")

    while True:
        data = conn.recv(1024).decode('utf-8')
        print(f"Received from {addr}: {data}")

        if data == "#" or data == "Exit":
            break

        reply = input(f"Reply to {addr}: ")
        conn.send(reply.encode('utf-8'))

        if reply == "#" or reply.lower() == "Exit":
            break

    conn.close()
    print(f"Connection with {addr} closed")

#setup of server
def main():
    host = '0.0.0.0'
    port = 12345

#Creates a socket using IPv4 (AF_INET) and TCP (SOCK_STREAM).
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Binds the socket to the specified host (0.0.0.0) and port (12345).
    server_socket.bind((host, port))
#Listens for incoming connections with a maximum queue size of 5.
    server_socket.listen(5)  # Listen for up to 5 connections

    print(f"Waiting for connections on port {port}")

    while True:
        conn, addr = server_socket.accept()

        # Start a new thread to handle the communication with the connected client
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    main()
