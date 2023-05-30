import threading
import time
import random
import socket


def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', 50007)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print("[S]: Got a connection request from a client at {}".format(addr))

    # send a intro message to the client.
    msg = " Welcome to CS 352!"
    csockid.send(msg.encode('utf-8'))

    dataFromClient = csockid.recv(1024)

    decoded = dataFromClient.decode()

    reversed = "\n".join([string[::-1] for string in decoded.split('\n')])

    # reversed = decoded[::-1]
    # reversedWithoutSpace = reversed[1:]

    f = open("outr-proj.txt", "w")
    f.write(reversed)
    f.close()

    # Note: Did this thing above ^^ because reversed left the first line empty and started message at 2nd line.

    # print("Received data is: " + decoded)

    # print("Reversed message is " + reversedWithoutSpace)

    csockid.send(reversed.encode('utf-8'))

    upped = decoded.upper()

    f = open("outup-proj.txt", "w")
    f.write(upped)
    f.close()

    #csockid.send(upped.encode('utf-8'))

    # Close the server socket
    ss.close()
    exit()


if __name__ == "__main__":
    t1 = threading.Thread(name='server', target=server)
    t1.start()

    print("Done.")
