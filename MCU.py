#!/usr/bin/python

import spidev
from wifi import Cell, Scheme
import RPi.GPIO as GPIO
import sys
import re

def Music_SendSong(title):
    speed = int(20000)

    spi_block_size = 4096
    
    # Read in file
    f = open(title, 'rb')
    bytes_read = f.read()
    f.close()
    
    # GPIO setup
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(11, GPIO.IN)
         
    # Convert read string to int representation
    bytes = []
    for byte in bytes_read:
        bytes.append(ord(byte))

    # Create SPI object with configuations 
    spi = spidev.SpiDev()
    spi.open(0,0)
    spi.max_speed_hz = speed
    
    # Send data in chunks
    print("Sending packets . . .")
    print("Sending initial 4 blocks")
    for init in range(4):
    	if(len(bytes) > 4096):
            r = spi.xfer2(bytes[:4096])
            bytes = bytes[4097:]
        else:
            r = spi.xfer2(bytes)
            bytes = []
    print("4 blocks sent, waiting on line ")
    while(len(bytes) > 0):
        while(GPIO.input(11) == GPIO.LOW):
        	pass
        #print("Pin went high")
        if(len(bytes) > 4096):
            r = spi.xfer2(bytes[:4096])
            bytes = bytes[4097:]
        else:
            r = spi.xfer2(bytes)
            bytes = []
    spi.close()

def WIFI_scanForNetworks():
    cells = Cell.all('wlan0')
    # Saved Wifi Networks
    #schemes = list(Scheme.all())

    return cells

def Voting_AddSong(songTitle, location):
    # Get current PHP file
    f = open('index.php', 'r')
    readLines = f.read()
    f.close()

    # Find title locations
    result = re.findall('value=.*</p>', readLines)
    print(result)

    # Insert title at location
    newLines = readLines

    # Rewrite file
    #f = open('index.php', 'w')
    #f.write(newLines)
    #f.close()


def Main():
    print("Staring MCU . . .")

    Voting_AddSong("dummy song", 3);
    
    print("Exiting MCU. . .")

Main()
