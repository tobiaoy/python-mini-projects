import threading
import socket

# we need to identify a host address for the server
host = '' # could be local host '127.0.0.1'
port = '' # avoid special/reserved ports

server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen # puts our server into listening mode to listen for connections

clients = [] # list where we will keep our clients
nicknames = [] # the nickname assigned to the client

# a func to broadcast messages to all clients
def broadcast(msg):
    for client in clients:
        client.send(msg)
        
# how do we want to handle connections
def handle(client):
    while True:
        try:
            message = client.recv(1024) # 1024 bytes
            broadcast(message)
        except Exception:
            ind = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[ind]
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break
        
def receive():
    while True:
        client, address = server.accept() # allows clients to connect
        print(f'connected with {str(address)}')
        
        client.send('NICK'.encode('ascii')) # a code word that the client will receive but the user can't see
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        
        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} joined the chat'.encode('ascii'))
        client.send('Connected to the server'.encode('ascii'))
        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        
# need to actually receive()