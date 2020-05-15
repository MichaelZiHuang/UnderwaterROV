'''
server.py
Designed by the BlueROV2 Iceberg Explorer CS capstone team for Jonathan Nash

This server is designed to be a network-attached passthrough that recieves signals from client.py.
This script will run on the BlueROV2's built in raspberry pi, and will interpret and pass signals 
through to a microcontroller that we put in place for this system, to allow for the remote user to
control custom ECE circuits through an attached series of electrical relays. The two scripts communicate 
using a simple TCP connection over the local network that the BlueROV2 already uses for it's control system.
'''

import time
import serial
import socket   

print("Connecting to arduino: ", end="")
ardu = serial.Serial('COM4',9600)#, timeout=.1)
# line = ardu.readline()
# print(line.decode().strip())

def send_serial(cmd):
    # time.sleep(5)
    print("Sending command to arduino: ", end="")
    ardu.write((cmd+'\r').encode())
    # time.sleep(1)
    
    print("done")

    # *** For use with arduino, not currently needed ***
    # The arduino sends back whether or not it recieved to command correctly
    # If it sends something with "Error" in it then it failed, otherwise it succeeded
    # This code was here for use with serial_to_GPIO.ino arduino code, not needed with the SSC-32U
    # line = ardu.readline()
    # print(line.decode().strip())
    # if "Error" in line.decode().strip():
    #     return 1
    # else:
    # *** END arduino error checking ***
    return 0

# next create a socket object 
s = socket.socket()          
print("Socket successfully created")
  
# reserve a port on your computer
# corresponds with client.py port
port = 3480                
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
print("socket binded to %s", port)
  
# put the socket into listening mode 
s.listen(5)      
print("socket is listening")            
  
# a forever loop until we interrupt it or  
# an error occurs 
while True: 
  
    # Establish connection with client. 
    c, addr = s.accept()      
    print('Got connection from', addr) 
    
    # recieve the sent command
    cmd = c.recv(1024) 
    # send the decoded command to our enslaved controller
    print("sending")
    res = send_serial(cmd.decode())
    print("res: ", res)
    # if we got a 0 it recieved the command, otherwise not sure
    if res > 0:
        c.send("fail".encode())
    else:
        c.send(cmd)
    
    # Close the connection with the client 
    c.close() 

ardu.close() 