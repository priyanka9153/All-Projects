import socket

def main():
    host = '0.0.0.0'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Waiting for connections on port {port}")

    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    while True:
        data = conn.recv(1024).decode('utf-8')
        print(f"Received from user2: {data}")

        if data == "#" or data == "Exit":
            break

        reply = input("Reply to user2: ")
        conn.send(reply.encode('utf-8'))

        if reply == "#" or reply == "Exit":
            break

    conn.close()
    print("Connection closed")

if __name__ == "__main__":
    main()
