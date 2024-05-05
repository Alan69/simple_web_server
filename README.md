# Simple Python Socket Server and Client

This repository contains a basic Python socket server and client implementation.

## Description

The server (`server.py`) and client (`client.py`) scripts demonstrate a simple communication mechanism using sockets in Python. The server listens for incoming connections from clients and echoes back any received messages. The client connects to the server and sends messages, then displays any echoed messages received from the server.

## Features

- **Server**:
  - Listens for incoming connections.
  - Echoes back messages received from clients.
  - Supports multiple client connections simultaneously.
  - Gracefully handles client disconnections and errors.

- **Client**:
  - Connects to the server.
  - Sends messages to the server.
  - Displays echoed messages received from the server.
  - Supports graceful termination.

## Usage

1. Start the server by running `python server.py`.
2. Run one or more instances of the client script using `python client.py`.
3. Enter messages in the client's terminal to send them to the server.
4. The server will echo back the messages to the clients.
5. Press Ctrl+C to exit the server or client gracefully.

## Requirements

- Python 3.x

Feel free to customize it further according to your specific project details and requirements!
