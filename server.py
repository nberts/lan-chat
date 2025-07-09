import socket
import threading
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='LAN Chat Server')
    parser.add_argument('--port',
                        type=int,
                        default=65432,
                        help='Port number (defult: 65432)')
    return parser.parse_args()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        try:
            if not message.endswith(b'\n'):
                message += b'\n'
            client.send(message)
        except:
            clients.remove(client)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"{nickname} joined the chat!")
        client.send('Connected to the server!\n'.encode('utf-8'))
        broadcast(f'{nickname} joined the chat!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    args = parse_arguments()
    HOST = '0.0.0.0'
    PORT = args.port

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    
    print(f"Server listening on {HOST}:{PORT}")
    receive()