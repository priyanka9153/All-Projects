import socket
import tkinter as tk
from tkinter import scrolledtext, simpledialog

class User2GUI:
    def __init__(self, master, host, port):
        self.master = master
        self.master.title("User2 - IM System")

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill='both')

        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((host, port))
        print("Connected to User1")

        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

        self.receive_messages()

    def receive_messages(self):
        while True:
            data = self.connection.recv(1024).decode('utf-8')
            self.text_area.insert(tk.END, f"User1: {data}\n")
            if data == "#":
                break

    def on_close(self):
        self.connection.close()
        self.master.destroy()

def main():
    host = '10.82.53.227'  # Replace with the actual IP address of user1
    port = 12345  # Use the same port number as user1

    root = tk.Tk()
    user2_gui = User2GUI(root, host, port)
    root.mainloop()

if __name__ == "__main__":
    main()