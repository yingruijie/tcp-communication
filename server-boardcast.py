import socket
import threading


def keyboard():
    global sock_l
    msg = ""
    while True:
        msg=input('Please input: ')
        if not msg:
            break
        else:
            for sock in sock_l:
                sock.send(msg.encode())
    return

if __name__ == "__main__":
    global sock_l
    sock_l = []

    tk=threading.Thread(target=keyboard,args=()) 
    tk.start()

    address='127.0.0.1' 
    port=12344 
    buffsize=1024     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((address,port))
    s.listen(3)   


    print("connecting to clients...")
    ii = 0
    while True:
        ii = ii + 1
        # create a new sock for the client
        clientsock,clientaddress=s.accept()
        print("connect to the " + str(ii) + "th client: ",clientaddress)
        sock_l.append(clientsock)

    s.close()
    