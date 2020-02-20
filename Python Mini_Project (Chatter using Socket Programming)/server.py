# Mini Project - Server

import socket

chat_msg=[]

recv_ip="127.0.0.1"                                                  #       localhost ipv4
recv_port=4444                                                       #       localhost port

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)                    #       creating a UDP socket

s.bind((recv_ip,recv_port))                                          #       binding ip and port with socket

choice=int(input("Enter 1 if you want to chat"))

while choice==1 :
    msg=s.recvfrom(100)
    recieved_msg=msg[0].decode('ascii')
    chat_msg.append(recieved_msg)
    ch=int(input("Do you want to see the recieved message, if so then enter 1 or enter any other number"))
    if ch==1 :
        print(recieved_msg)
    else :
        continue
    chs=int(input("Do you want to reply, if so then enter 1"))
    if chs==1 :
        rply=input("Enter Your Reply")
        s.sendto(rply.encode('ascii'),msg[1])                        #       sending reply to sender
    else :
        s.sendto("",msg[1])
    choice=int(input("Do you want to continue chat, if so then enter 1"))
    s.sendto(str(choice).encode('utf-8'),msg[1])
    
s.close()
print("Connection Terminated")