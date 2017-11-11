# line-detection
UTRA ART 2017 Vision white line detection project



## Desciption:
The aim of this project is to detect white lines on images.


## Installation: 

### OpenCV installation 
Note: This installation is only for Linux operating systems. It is recommended that you have Ubuntu or Mint on virtual machine or dual booted into your PC

Step 1: Update any pre-installed packages
 $ sudo apt-get update
 $ sudo apt-get upgrade
 
Step 2: Install Python 3
 
 Check if you have Python already installed by checking the version
 
 $ python --version
 or
 $ python3 --version
 
 It is recommended that you have Python 3.4+ because most of the code is written in Python 3
 
 Installing Python3
 $ sudo apt-get install python3

Step 3: Installing pip3
 Pip is a package management system used to install and manage software packages written in Python. Pip3 is used to install packages for    python3
 $ sudo apt-get -y install python3-pip
 
Step 4: Installing numpy and matplotlib for Python3
If you could install pip3 without any issues, then install numpy and matplotlib
$ pip3 install numpy
$ pip3 install matplotlib

Step 5: Installing OpenCV from Pip3
 $ pip3 install opencv-python

Step 5: Validating the install
Run Python 3 on terminal
$ python3
and try importing the OpenCV library
>> import cv2
>> import numpy as np
>> from matplotlib import pyplot as plt
If you get no errors it means that you have successfully installed OpenCV, numpy and matplotlib on your Linux machine

If the above installation gives you errors then the following link points to a more rigorous installation of OpenCV
