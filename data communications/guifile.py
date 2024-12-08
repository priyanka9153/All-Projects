import socket
import tkinter as tk
from threading import Thread

class ServerGUI:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []  # Keep track of connected clients

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

        self.root = tk.Tk()
        self.root.title("Server")

        self.text_area = tk.Text(self.root, state='disabled')
        self.text_area.pack(pady=10)

        Thread(target=self.accept_connections).start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def accept_connections(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            self.text_area.config(state='normal')
            self.text_area.insert('end', f"Connection established with {client_address}\n")
            self.text_area.config(state='disabled')

            # Keep track of connected clients
            self.clients.append(client_socket)

            Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break

                # Display received message in the GUI
                self.text_area.config(state='normal')
                self.text_area.insert('end', f"Received: {data}\n")
                self.text_area.config(state='disabled')

                # Send the same message back to the client
                self.send_message(client_socket, f"Server: {data}")

            except ConnectionResetError:
                break

    def send_message(self, client_socket, message):
        try:
            client_socket.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error sending message: {e}")

    def on_closing(self):
        # Close all client sockets
        for client_socket in self.clients:
            client_socket.close()

        self.server_socket.close()
        self.root.destroy()

if __name__ == "__main__":
    user1_host = "0.0.0.0"  # Replace with the IP address of user1
    user1_port = 12345  # Replace with the desired port number
    ServerGUI(user1_host, user1_port)
