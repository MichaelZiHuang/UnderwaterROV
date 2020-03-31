import time
import serial
import socket   

print("Connecting to arduino: ", end="")
ardu= serial.Serial('COM3',9600)#, timeout=.1)
line = ardu.readline()
print(line.decode().strip())

def send_serial(cmd):
    # time.sleep(5)
    print("Sending command to arduino: ", end="")
    ardu.write(cmd.encode())
    # time.sleep(1)
    line = ardu.readline()
    print(line.decode().strip())

    if "Error" in line.decode().strip():
        return 1
    else:
        return 0

# next create a socket object 
s = socket.socket()          
print("Socket successfully created")
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
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
    
    # send a thank you message to the client.  
    cmd = c.recv(1024) 
    res = send_serial(cmd.decode())
    if res > 0:
        c.send("fail".encode())
    else:
        c.send(cmd)
    
    # Close the connection with the client 
    c.close() 

# TODO will never reach here
ardu.close() 