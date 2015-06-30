#!/usr/bin/python

import spidev
from wifi import Cell, Scheme
import RPi.GPIO as GPIO
import sys
import re
from constants import *
import glob

# Make changes live vs dev
VOTING_HOMEPAGE = VOTING_DEV

#####################################################################

def Music_SendSong(title, speed):
    speed = int(speed)

    spi_block_size = SPI_MAXBLOCKSIZE
    
    # Read in file
    f = open(title, 'rb')
    bytes_read = f.read()
    f.close()
    
    # GPIO setup
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(GPIO_BUFFERFULL, GPIO.IN)
         
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
    for init in range(SPI_BUFFERSIZE):
    	if(len(bytes) > SPI_MAXBLOCKSIZE):
            r = spi.xfer2(bytes[:SPI_MAXBLOCKSIZE])
            bytes = bytes[SPI_MAXBLOCKSIZE + 1:]
        else:
            r = spi.xfer2(bytes)
            bytes = []
    print("4 blocks sent, waiting on line ")
    while(len(bytes) > 0):
        while(GPIO.input(GPIO_BUFFERFULL) == GPIO.LOW):
        	pass
        #print("Pin went high")
        if(len(bytes) > SPI_MAXBLOCKSIZE):
            r = spi.xfer2(bytes[:SPI_MAXBLOCKSIZE])
            bytes = bytes[SPI_MAXBLOCKSIZE + 1:]
        else:
            r = spi.xfer2(bytes)
            bytes = []
    spi.close()

#####################################################################

def WIFI_scanForNetworks():
    cells = Cell.all(WIRELESS)
    # Saved Wifi Networks
    #schemes = list(Scheme.all())

    return cells

#####################################################################

def Voting_AddSong(songTitle, location):
    target = str(location) + '"/>.*</p>'
    replaceTarget = '>.*<'
    replaceContent = '>' + songTitle + '<'

    # Get current PHP file
    f = open(VOTING_HOMEPAGE, 'r')
    readLines = f.read()
    f.close()

    # Find title locations
    result = re.findall(target, readLines)
    result = re.sub(replaceTarget, replaceContent, result[0])

    # Insert title at location
    newLines = re.sub(target, result, readLines)

    # Rewrite file
    f = open(VOTING_HOMEPAGE, 'w')
    f.write(newLines)
    f.close()


#####################################################################

def Voting_PopulateBallet(songDirectoryPath):

    # Get list of songs in directory path
    listOfFiles = glob.glob(songDirectoryPath + "/*.m4a")
    print(listOfFiles)

    # Clean list
    cleanList = []
    for song in listOfFiles:
        cleanSong = re.match("(" + songDirectoryPath + "/)(.*)(.m4a)", song)
        cleanList.append(cleanSong.group(2))
    print(cleanList)

    # Generate PHP code for song list

    
    # Get current PHP file
    #f = open(VOTING_HOMEPAGE, 'r')
    #readLines = f.read()
    #f.close()

    # Replace choice list with selection
    
    # Rewrite file
    #f = open(VOTING_HOMEPAGE, 'w')
    #f.write(newLines)
    #f.close()

#####################################################################

def Main():
    print("Staring MCU . . .")

    Voting_PopulateBallet("music")
    
    print("Exiting MCU. . .")

Main()
