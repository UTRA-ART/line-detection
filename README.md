# line-detection
UTRA ART 2017 Vision white line detection project



Desciption:
The aim of this project is to detect white lines on images.


Installation: 

#OpenCV installation 
Note: This installation is only for Linux operating systems. It is recommended that you have Ubuntu or Mint on virtual machine or dual booted into your PC


Step 1: Install prerequisites : Upgrade any pre-installed packages:

$ sudo apt-get update
$ sudo apt-get upgrade

Install developer tools used to compile OpenCV 3.0:

$ sudo apt-get install build-essential cmake git pkg-config

Install libraries and packages used to read various image and videos formats from disk:

$ sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev

Install GTK so we can use OpenCV’s GUI features:

$ sudo apt-get install libgtk2.0-dev

Install packages that are used to optimize various functions inside OpenCV, such as matrix operations:

$ sudo apt-get install libatlas-base-dev gfortran

Step 2: Setup Python (Part 1)

Download pip , a Python package manager, installed for Python 3:

$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python3 get-pip.py

Use pip3 install to setup virtualenv and virtualenvwrapper :

$ sudo pip3 install virtualenv virtualenvwrapper

Now update the ~/.bashrc file (place at the bottom of the file):

# virtualenv and virtualenvwrapper
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
$ source ~/.bashrc
$ mkvirtualenv cv

Step 2: Setup Python (Part 2)

we’ll need to install the Python 3.4+ headers and development files:

$ sudo apt-get install python3.4-dev

OpenCV represents images as NumPy arrays, so we need to install NumPy into our cv virtual environment:

$ pip install numpy

Step 3: Build and install OpenCV 3.0 with Python 3.4+ bindings

$ cd ~
$ git clone https://github.com/Itseez/opencv.git
$ cd opencv
$ git checkout 3.0.0
$ cd ~
$ git clone https://github.com/Itseez/opencv_contrib.git
$ cd opencv_contrib
$ git checkout 3.0.0

Time to setup the build:

$ cd ~/opencv
$ mkdir build
$ cd build
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D BUILD_EXAMPLES=ON ..

Let's start OpenCV compile process :

$ make -j4

Assuming OpenCV 3.0 compiled without error, you can now install it on your system:

$ sudo make install
$ sudo ldconfig

Step 4: Sym-link OpenCV 3.0

If you’ve reached this step, OpenCV 3.0 should now be installed in /usr/local/lib/python3.4/site-packages/.

Notice that the directory points to python3.4, this part must be changed depending on which python3 version you have.

Here, our OpenCV bindings are stored under the name cv2.cpython-34m.so

However, in order to use OpenCV 3.0 within our cv virtual environment, we first need to sym-link OpenCV into the site-packages directory of the cv environment, like this: (Be sure to take note of cv2.cpython-34m.so)

$ cd ~/.virtualenvs/cv/lib/python3.4/site-packages/
$ ln -s /usr/local/lib/python3.4/site-packages/cv2.cpython-34m.so cv2.so

Notice how I am changing the name from cv2.cpython-34m.so to cv2.so — this is so Python can import our OpenCV bindings using the name cv2 .

Step 5: Test out the OpenCV 3.0 and Python 3.4+ install

$ workon cv
$ python
>>> import cv2
>>> cv2.__version__
'3.0.0' 
