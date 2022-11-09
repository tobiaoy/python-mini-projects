import socket
import threading

nickname = input('Please choose a nickname: \n')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('', '')) # rather than bind to a host we will be connecting to an IP and a port

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except Exception:
            print('An error occurred')
            client.close()
            break
        
def write():
    while True:
        msg = f'{nickname}: {input('')}'
        client.send(msg.encode('ascii'))
        
receive_thread = threading.Thread(target=receive)
receive_thread.start()

writing_thread = threading.Thread(target=write)
writing_thread.start()
