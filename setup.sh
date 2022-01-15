#!/bin/bash
# Update packages on your Raspberry Pi OS.
sudo apt-get update
sudo apt-get install -y python3-pip
sudo pip3 install --upgrade setuptools
sudo apt-get install -y i2c-tools
export CFLAGS=-fcommon
pip3 install RPi.GPIO==0.7.0
pip3 install install Adafruit-Blinka==6.17.0
pip3 install opencv-python==4.5.3.56
pip3 install adafruit-circuitpython-ssd1306==2.12.3
pip3 install tflite-runtime==2.7.0
pip3 install argparse
pip3 install numpy==1.21.4
pip3 install tflite-support==0.3.1
