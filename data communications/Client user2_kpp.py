import socket

def main():
    host = '192.168.12.132'  # Replace with user1's IP address
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    client_socket.connect((host, port))

    while True:
        message = input("Talk to user1: ")
        client_socket.send(message.encode('utf-8'))

        if message == "#" or message == "Exit":
            break

        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received from user1: {data}")

        if data == "#" or data == "Exit":
            break

    client_socket.close()
    print("Connection closed")


if __name__ == "__main__":
   main()