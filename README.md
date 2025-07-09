# LAN Chat Application

A simple Python-based LAN chat application that enables multiple users to communicate over a local network.

## Features
- Real-time messaging over LAN
- Multiple client support
- Nickname-based identification
- Join/Leave notifications
- Clean user interface with command prompt
- Exit with /quit command

## Requirements
- Python 3.x
- No additional packages required (uses built-in socket and threading libraries)

## Usage

### Starting the Server
```bash
# Start with default port (65432)
python3 server.py

# Start with custom port
python3 server.py --port 12345
```
### Starting the Client
```bash
# Connect to server
python3 client.py --host SERVER_IP_ADDRESS

# Connect to server with custom port
python3 client.py --host SERVER_IP_ADDRESS --port 12345
```

### Chat Commands
- Type your message and press enter to send.
- Type /quit to exit the chat

### Setup Instructions
1. Clone the repository
    git clone https://github.com/YOUR_USERNAME/lan-chat.git
    cd lan-chat
2. Start the server on one machine
3. Connect clients from other machines using the server's IP address.

## Note
Make sure all devices are on the same local netwwork and the port is not blocked by firewall.
