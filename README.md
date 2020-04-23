# Capstone Project - Iceberg Explorer
<h1>Introduction</h1>
This project will focuses on expanding an already existing proposal by our client. Their central goal is to create new methods of measuring active glacial melt in the arctic. The final product this project is to provide an ROV capable of traveling 30m underwater in the Arctic ocean and be able to scan a timelapse of the changing topography of a melting glacier. With this, researchers will another method to accurately measure glacier melt without putting themselves in danger.

<h1>Current Status</h1>

To Do:
* Custom Controls with IC32 Hardware

<p> With the advent of the COVID-19, the goals of this project have changed significantly. We still plan on completing the above To-do:

<h1>How to Run</h1>
This software requires both hardware and software to run, these are notably as follows:

Software:
* Agisoft (Licensed)
* Python Packages (detailed further in specific sections

Hardware:
* Arduino or an otherwise developed system
* A camera OR pre-recorded video

<h1>Custom Controls</h1>

The custom control software contains three seperate pieces that work together to send signals to a relay controller.
The client.py program contains the graphical interface for a user to enable or disable relay controls. 
The server.py program is connected to by the client.py program, and acts as a passthrough to send commands from client.py to the hardware controller. 
The third element, a connected serial device, takes commands pass through from client.py and interprets them to enable or disable a signal to a relay controller, which will be used to control external devices on the ROV.
Instructions for running the custom control software:
1. Start the server by running "py server.py". The server script should have connected to the serial device, and will be waiting for a connection from the client. 
2. Start the client by running "py client.py". The client will open up a GUI and will wait for user input
3. Pressing a button on the client GUI will create a connection to the server, and send a command to switch that corresponding pin. The pin on the serial device should then be switched, and the color of the button in the GUI should change between red and green, indicating off and on.


<h1>Agisoft Demo</h1>
