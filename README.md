# line-detection
UTRA ART 2017 Vision white line detection project



## Desciption:
The aim of this project is to detect white lines on images. The folder test image database contains all the images used as test cases.


## Installation: 

### OpenCV installation 
Note: This installation is only for Linux operating systems. It is recommended that you have Ubuntu or Mint on virtual machine or dual booted into your PC

#### Step 1: Update any pre-installed packages

    $ sudo apt-get update
 
    $ sudo apt-get upgrade
 
#### Step 2: Install Python 
 
Check if you have Python already installed by checking the version
 
    $ python --version
 
It is recommended that you have Python 3.4+ because most of the code is written in Python 3
 
Installing Python3
 
    $ sudo apt-get install python

#### Step 3: Installing pip
Pip is a package management system used to install and manage software packages written in Python. Pip3 is used to install packages for python3
 
    $ sudo apt-get -y install python-pip
 
#### Step 4: Installing numpy and matplotlib for Python3
If you could install pip3 without any issues, then install numpy and matplotlib

    $ pip install numpy

    $ pip install matplotlib

#### Step 5: Installing OpenCV from Pip3

    $ pip install opencv-python

#### Step 5: Validating the install

Run Python 3 on terminal

    $ python

and try importing the OpenCV library
>> import cv2

If you get no errors it means that you have successfully installed OpenCV
>> import numpy as np

If you get no errors it means that you have successfully installed numpy

>> from matplotlib import pyplot as plt

If you get no errors it means that you have successfully installed matplotlib

If the above installation gives you errors then the following link points to a more rigorous installation of OpenCV
https://stackoverflow.com/questions/37188623/ubuntu-how-to-install-opencv-for-python3

_NOTE_: If you installed or tried to install ROS(Robotic Operating System), it is likely that you already have OpenCV installed but for Python 2.7+ The UTRA team requires you to use Python 3+. You might run into issues if you try to import cv2 from python 3 as the python path is edited to import from ROS dist. This is because of edits made to the bash file during the ROS installation.
The workaround to this problem would be open your bash file in vim or gedit edit. Your bash file will be located in /home/username/.bashrc


**YOU SHOULD NOT MAKE ANY CHANGES TO YOUR BASH FILE OTHER THAN ONE SHOWN BELOW, MAKE SURE YOU KNOW EXACTLY WHAT YOU ARE DOING BEFORE YOU EDIT THE BASH FILE**

Go to the above directory and press Ctrl + H to show hidden files then open the bash file in an editor of your choice

Then remove the following line from the end of your bash file

/opt/ros/kinetic/lib/python2.7/dist-packages

## Work Progress
### Step1 : Detecting the white colour inside the image
Using gimp image editor's colour picker tool the max and min BGR values for the a given colour in a test image can be calculated. Once they are calculated they are passed into converter.py as system arguments to obtain the max and min HSV values as arrays.
These values are then to be passed into the lower range and upper range arrays in the image.py file and the test image's name should be changed as necessary in the converter.

This code just converts all of the green colour in the image to white and everything else to black so this does not yet account for humans and cones.

Test image:
![alt text](https://github.com/UTRA-CV/line-detection/blob/master/colourdetector/img_3.jpg "testimage")
After colour detection:
![alt text](https://github.com/UTRA-CV/line-detection/blob/master/colourdetector/mask.jpg "output")


