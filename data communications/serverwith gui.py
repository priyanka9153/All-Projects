import socket
import threading

def handle_client(conn, addr):
    print(f"Connection established with {addr}")

    try:
        while True:
            data = conn.recv(1024).decode('utf-8')
            print(f"Received from {addr}: {data}")

            if data == "#" or data == "Exit":
                break

            reply = input(f"Reply to {addr}: ")
            conn.send(reply.encode('utf-8'))

            if reply == "#" or reply.lower() == "Exit":
                break

    except Exception as e:
        print(f"Error handling client {addr}: {e}")

    finally:
        conn.close()
        print(f"Connection with {addr} closed")

def main():
    host = '0.0.0.0'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind((host, port))
        server_socket.listen(5)  # Listen for up to 5 connections
        print(f"Waiting for connections on port {port}")

        while True:
            conn, addr = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

    except Exception as e:
        print(f"Error in the server: {e}")

    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
