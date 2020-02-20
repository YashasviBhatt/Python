# Mini Project - Client


import socket

chat_msg=[]

# creating a localhost messaging server
recv_ip="127.0.0.1"                                              #       localhost ipv4
recv_port=4444                                                   #       localhost port

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)                #       creating a UDP socket

choice=int(input("Enter 1 if you want to chat"))                 

while choice==1 :
    msg=input("Enter your Message")                              #       input message by sender
    sending_msg=msg.encode('ascii')                              #       encoding message character from byte to ascii type
    chat_msg.append(msg)
    s.sendto(sending_msg,(recv_ip,recv_port))                    #       message send to reciever
    recv_msg=s.recvfrom(100)
    recieved_msg=recv_msg[0].decode('ascii')
    chat_msg.append(recieved_msg)
    ch=int(input("Do you want to see the recieved message, if so then enter 1 or enter any other number"))
    if ch==1 :
        print(recieved_msg)
    else :
        continue
    recieved_choice=s.recvfrom(1)
    choice=recieved_choice[0].decode('utf-8')
print("Connection Terminated by Reciever")
s.close()