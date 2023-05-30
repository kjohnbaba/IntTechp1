import threading
import time
import random
import socket


def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    # Define the port on which you want to connect to the server
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)

    # untested code to send string from client to server

    #testmessage = "hello"

    f = open("in-proj.txt", "r")

    testmessage = f.read()
    #testmessage.split('\n')
    f.close()
    cs.send(testmessage.encode())


    # Receive data from the server
    data_from_server = cs.recv(512)
    print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

    # data_from_server = cs.recv(512)
    # print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))


    # data_from_server = cs.recv(512)
    # print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))



    #data_from_server = cs.recv(1024)
    #print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

    # close the client socket
    cs.close()
    exit()


if __name__ == "__main__":

    t2 = threading.Thread(name='client', target=client)
    t2.start()

    print("Done.")
