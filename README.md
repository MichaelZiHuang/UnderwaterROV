# Capstone Project - Iceberg Explorer
<h1>Introduction</h1>
This project will focuses on expanding an already existing proposal by our client. Their central goal is to create new methods of measuring active glacial melt in the arctic. The final product this project is to provide an ROV capable of traveling 30m underwater in the Arctic ocean and be able to scan a timelapse of the changing topography of a melting glacier. With this, researchers will another method to accurately measure glacier melt without putting themselves in danger.

<h1>Current Status</h1>
* Custom Controls require physical pairing with ROV
* Agisoft requires additional accuracy tests

<h1>Code Review Feedback</h1>
 On May 4th, our Team participated in a Code Review where 2 other teams critiqued our design. We will address them here.
 
 *  "Fix comment at server.py:31, wrong port number" - Changed, removing deprecated code and comments.
 *  "Remove using namespace std;" - Denied, we did not see a reason as to why this is a problem
 *  "Add Error checking or remove commented code" - Commented code removed
 *  "Not all functions are clear"  - Added more descriptive function headers to custom control code
 *  "Lighting issue on GUI" - Noted, may change at a later date as this is a prototype GUI, not for production usage

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

The Agisoft demo has 2 processes in its functionality.
The first process is a python script that takes in any number of video inputs and splices each video into a respective directory containing each individual frame of the video.
The second process is running Agisoft PRO and in the Agisoft console you enter the directory names of the spliced images.

1. Start splicing the video by running the command "py videosplicer.py IMG_3794.mp4". This will create a new directory containing the individual frames of that video.
2. After this script finishes, it will output the --image_folder flag that will be used in the corresponding steps.
3. Open Agisoft PRO. Open up the run script terminal or by "ctrl + r". Click the folder icon that it provides, and find the script createModel.py that is located in the Scripts/Modeling directory.
4. For the arguments the --image_folder is required and can be copied and pasted from the output of the splice script. It will then take nargs, any number of arguments, that correspond to folder names that are located in that directory listed in the output of the first script.
> an example of a completed arguments field could be: "--image_folder D:\underwaterrov\UnderwaterROV\Scripts\Modeling IMG_3794"

5. This will create a chunk and start modeling for the photos that were in the IMG_3794 directory.
6. Click the run scripts button, and the modeling process will begin. Note this entire process all the way to build the dense cloud can take a good amount of time.
