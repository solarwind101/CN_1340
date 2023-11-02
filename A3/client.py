import socket
import sys

s_host = '127.0.0.1'
s_port = 60134

#================= CONNECT TO THE SERVER ===========================#
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((s_host, s_port))
    print("Connected to server:", s_host)
except IOError:
    print("\n\n\a\t\tUndefined Connection Error Encountered")
    sys.exit()
#===================================================================#

#================ Query & Response =================================#
data = ""
data += client_socket.recv(1024).decode()
print(data)

while True:
    Qno = input("Please enter Question no. to get the answer: ")   # Client: Questiono no?
    client_socket.send(str(Qno).encode())                      # Client: sending to server....
    if int(Qno) in [1,2,3,4,5,6,7,8,9,10]:
        response = client_socket.recv(2048).decode()               # Client: Receving the data ....
        print(response)
           
        print(client_socket.recv(1024).decode())                        # Server : Follow up question?
        response = input()                                              # Client : Wait, asking the user.
        client_socket.send(response.encode())                           # Client : have a look, I'm sending you what to do.
        if response.lower()!='y':                                       # Client : Condition!  Let me check as well if I need to break the loop
            break     
    else:
        print(client_socket.recv(1024).decode())                          

# Closing the connection ....

client_socket.close()

#=============================== THE END ============================#