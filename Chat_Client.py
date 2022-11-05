from copyreg import pickle
import socket
import sys
import DES as des
import Utils as utils
import threading
import time

username  = input("Enter username: ")
key = input('Enter key: ')
while len(key) != 8:
    key = input('Key must be 8 characters long. Enter key: ')

key = utils.str_to_hex(key)


server_address = ('localhost', 5000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

def read_logs():
    data = client_socket.recv(1024)
    message_len = int(data.decode().split("\r\n\r\n",1)[0])
    if message_len > 0:
        incoming_message = data.decode().split("\r\n\r\n",1)[1]

        if len(incoming_message) < message_len:
            data = client_socket.recv(message_len - len(incoming_message))
            time.sleep(0.2)
            incoming_message += data.decode()
        
        logs = incoming_message.split("\r\n\r\n")
        for log in logs:
            print(des.DES_Decrypt(log, key))
    else:
        return

def handle(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                print("Disconnected from server")
                client_socket.close()
                sys.exit(0)
            else:
                message_len = int(data.decode().split("\r\n\r\n",1)[0])
                incoming_message = data.decode().split("\r\n\r\n",1)[1]

                while len(incoming_message) < message_len:
                    data = client_socket.recv(1024)
                    incoming_message += data.decode()
                    
                print(des.DES_Decrypt(incoming_message, key))
    except:
        print("Disconnected from server")
        client_socket.close()
        sys.exit(0)

try:
    
    read_logs()
    thread = threading.Thread(target=handle, args=(client_socket,)).start()
    
    try:
        while True:
            message = input(username +"(You): ")
            encrypted = des.DES_Encrypt(username + ": " + message, key)
            time.sleep(0.1)
            sent = str(len(encrypted)) + "\r\n\r\n" + encrypted
            # print("Sending " + sent)
            client_socket.send(sent.encode())
            
    except KeyboardInterrupt:
        print("Closed")
        client_socket.close()
        sys.exit(0)
        
       

except KeyboardInterrupt:
    print("Disconnnected from " + str(client_socket.getpeername()))
    client_socket.shutdown(socket.SHUT_RDWR)
    client_socket.close()
    sys.exit(0)