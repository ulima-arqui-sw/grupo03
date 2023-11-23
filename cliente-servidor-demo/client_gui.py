import socket
import tkinter as tk
from tkinter import Entry, Button, Text, Scrollbar, END

class ClientApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Client")

        self.message_entry = Entry(master)
        self.message_entry.pack(pady=10)

        self.send_button = Button(master, text="Send", command=self.send_message)
        self.send_button.pack()

        self.text_area = Text(master, height=10, width=50)
        self.text_area.pack(pady=10)

        self.scrollbar = Scrollbar(master, command=self.text_area.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.text_area.config(yscrollcommand=self.scrollbar.set)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_address = ('localhost', 12345)
        self.client_socket.connect(server_address)

    def send_message(self):
        message = self.message_entry.get()

        self.client_socket.sendall(message.encode())

        self.display_message(f"Sent: {message}")

        self.message_entry.delete(0, END)

        data = self.client_socket.recv(1024)

        self.display_message(f"Received: {data.decode()}")

    def display_message(self, message):
        self.text_area.insert(END, message + "\n")
        self.text_area.see(END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClientApp(root)
    root.mainloop()
