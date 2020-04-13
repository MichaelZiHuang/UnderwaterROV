# Import socket module 
import socket  
from tkinter import Tk, Label, Button       
          
  
# Define the port on which you want to connect 
port = 3480                 
  
# Sends a serial message to a remove server on the BlueROV, which sends the message to the heater controller
# Format: "on pin#" to turn on, "of pin#" to turn off. pin# range 1-12 currently with arduino nano
# pin: pin number to change
# state_to: state we want to change the pin to (False for off, True for on)
def send_serial(pin, state_to):
    # Create a socket object 
    s = socket.socket()  

    # connect to the server on local computer 
    s.connect(('127.0.0.1', port)) 

    if state_to:
        cmd = "on " + str(pin)
    else:
        cmd = "of " + str(pin)

    s.send(cmd.encode())
    # receive data from the server 
    res = s.recv(1024).decode()
    print("pin: ", pin)
    print(res)
    # close the connection 
    s.close()

    if res == cmd:
        return 0
    elif res == "fail":
        return 1
    else:
        return 2 

# Define dictionaries to hold the pin numbers and states of the legs that correspond to the graphical names
# Pin numbers are the pin numbers that are sent to the arduino, so these would need to be changed if hardware changed
# For the states, False means off, True means on
legs_to_iopins = {'Leg 1 Forward': 1,
                  'Leg 2 Forward': 2,
                  'Leg 3 Forward': 3,
                  'Leg 1 Back': 4,
                  'Leg 2 Back': 5,
                  'Leg 3 Back': 6}

legs_to_state = {'Leg 1 Forward': False,
                  'Leg 2 Forward': False,
                  'Leg 3 Forward': False,
                  'Leg 1 Back': False,
                  'Leg 2 Back': False,
                  'Leg 3 Back': False}

class HeaterGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        # Initialize buttons for each leg
        self.buttons = {}
        for leg in legs_to_iopins:
            self.buttons[leg] = Button(master, text=leg, command=lambda x=leg: self.toggle_leg(x), bg="red")
            self.buttons[leg].pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def toggle_leg(self, leg):
        # Send the pin number to the arduino 
        res = send_serial(legs_to_iopins[leg], not legs_to_state[leg])

        # Check to make the arduino recieved the pin
        if res == 0:
            # Success, change state and color
            legs_to_state[leg] = not legs_to_state[leg]
            
            if legs_to_state[leg]:
                color = "light green"
            else:
                color = "red"

            self.buttons[leg].configure(bg = color)

root = Tk()
my_gui = HeaterGUI(root)
root.mainloop()    