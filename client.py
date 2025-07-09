import socket
import threading
import argparse
import random

COLORS = [
    '\033[91m', #bright red
    '\033[92m', #bright green
    '\033[93m', #bright yellow
    '\033[94m', #bright blue
    '\033[95m', #bright magenta
    '\033[96m', #bright cyan   
]

BOLD = '\033[1m'
RESET = '\033[0m'

nickname_colors = {}
color_index = 0

def get_color(nickname):
    global color_index
    if nickname not in nickname_colors:
        nickname_colors[nickname] = COLORS[color_index % len(COLORS)]
        color_index += 1
    return nickname_colors[nickname]

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

def format_message(message):
    try:
        if ': ' in message:
            nickname, content = message.split(': ', 1)
            color = get_color(nickname)
            return f"{color}{BOLD}{nickname}{RESET}:{content}"
        return message
    except:
        return message

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                formatted_message = format_message(message)
                if message.endswith('\n'):
                    print(f"\r{formatted_message}--> ", end='', flush=True)
                else:
                    print(f"\r{formatted_message}\n--> ", end='', flush=True)
        except:
            if not client._closed:
                print("\nAn error occurred!")
            break
    import sys
    sys.exit(0)

def write():
    print("\n{BOLD}Start chatting! Type /quit to exit.{RESET}")
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


