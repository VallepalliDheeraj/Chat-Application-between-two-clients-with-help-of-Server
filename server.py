import socket
import threading

HOST = 'localhost' # Set to '0.0.0.0' to allow connections from any IP address
PORT = 9100

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = {}
nicknames = []

def broadcast(message, sender):
    nickname = clients[sender]
    message_with_nickname = f"{nickname}: {message.decode('ascii')}"
    for client in clients:
        if client != sender:
            client.send(message_with_nickname.encode('ascii'))

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICKNAME".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients[client] = nickname

        print(f"Nickname of the client is {nickname}!")
        broadcast(f"{nickname} joined the chat!".encode('ascii'), client)
        client.send('Connected to the server!'.encode('ascii'))

        threading.Thread(target=handle, args=(client,)).start()

print("Server running...")
receive()