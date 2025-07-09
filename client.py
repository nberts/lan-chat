import socket
import threading
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='LAN Chat Client')
    parser.add_argument('--host',
                        type=str,
                        required=True,
                        help='Server IP address to connect to')
    parser.add_argument('--port',
                        type=int,
                        default=65432,
                        help='Port number (defult: 65432)')
    return parser.parse_args()

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                if message.endswith('\n'):
                    print(f"\r{message}--> ", end='', flush=True)
                else:
                    print(f"\r{message}\n--> ", end='', flush=True)
        except:
            if not client._closed:
                print("\nAn error occurred!")
            break
    import sys
    sys.exit(0)

def write():
    print("\n Start chatting! Type /quit to exit.")
    print("--> ", end='', flush=True)
    while True:
        try:
            user_input = input()
            if user_input.lower() == '/quit':
                print("Leaving chat...")
                client.close()
                import sys
                sys.exit(0)
            if user_input:
                message = f'{nickname}: {user_input}'
                client.send(message.encode('utf-8'))
                print("--> ", end='', flush=True)
        except:
            break


if __name__ == "__main__":
    args = parse_arguments()

    nickname = input("Choose your nickname: ")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((args.host, args.port))
    
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()
    
    write_thread = threading.Thread(target=write)
    write_thread.start()


