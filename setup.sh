#!/bin/bash
sudo apt-get install -y python3-pip
sudo pip3 install --upgrade setuptools
sudo apt-get install -y i2c-tools
export CFLAGS=-fcommon
pip3 install RPi.GPIO==0.7.0
pip3 install install Adafruit-Blinka==6.17.0
pip3 install opencv-python==4.5.3.56
pip3 install adafruit-circuitpython-ssd1306
pip3 install tflite-runtime==2.7.0
pip3 install argparse
pip3 install numpy==1.21.4
