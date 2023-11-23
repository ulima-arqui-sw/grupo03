import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
server_socket.bind(server_address)

server_socket.listen(1)
print(f"Server is listening on {server_address}")

while True:
    print("Waiting for a connection...")
    connection, client_address = server_socket.accept()

    try:
        print(f"Connection from {client_address}")

        data = connection.recv(1024)
        print(f"Received: {data.decode()}")
        connection.sendall(data)

    finally:
        connection.close()
