#!/usr/bin/python
from CONSTANTS import *
import RPi.GPIO as GPIO
import spidev
import sys
from time import *

class SPI():

	def __init__(self):
		self.spi = spidev.SpiDev()
		self.spi.open(0,0)

		# GPIO Setup
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)

		# Message sending signal pin calibration
		GPIO.setup(GPIO_SENDMESSAGE, GPIO.OUT)
		GPIO.output(GPIO_SENDMESSAGE, True)

		# Buffer full signal pin setup
		GPIO.setup(GPIO_BUFFERFULL, GPIO.IN)

		# Ready to micro ready to send via SPI, GPIO signal
		GPIO.setup(GPIO_RECEIVE, GPIO.IN)

	def __del__(self):
		self.spi.close

	#####################################################################
	#
	#	SEND LIST OF BYTES VIA SPI
	#
	#	Sends a list of bytes via SPI, preventing a stack overflow,
	#	limiting the number of bytes passed to the spidev moethod
	#	xfer2. Sends at speed specified.
	#
	#####################################################################

	def SendBytes(self, listOfBytes, speed):
		spi = self.spi
		speed = int(speed)
		spi_block_size = SPI_MAXBLOCKSIZE
		spi.max_speed_hz = speed

		if(len(listOfBytes) > SPI_MAXBLOCKSIZE):
				r = spi.xfer2(listOfBytes[:SPI_MAXBLOCKSIZE])
				listOfBytes = listOfBytes[SPI_MAXBLOCKSIZE + 1:]
		else:
			r = spi.xfer2(listOfBytes)
			listOfBytes = []

		return listOfBytes

	#####################################################################
	#
	#	SEND A MENU CHOICES AND RECEIEVE RESPONSE VIA SPI
	#
	#	Utilizes the SendStringMessage function to send a menu of
	#	choices and wait for to receive a response via SPI, based on
	#	signal from designated GPIO pin. Returns the response received
	#	via SPI. Returns None if bad receieve.
	#
	#	TODO: Add timeout feature, perhaps activated by arg
	#			that starts when GPIO pin asserted
	#
	#####################################################################
	def SendMenuChoices(self, menu, bytesToReceive=MENURESPONSESIZE):
		response = ""

		# Send menu of choices
		self.SendStringMessage(menu)

		# Wait for GPIO signal stating ready for micro to send response
		# Receieve set number of byte(s) for response
		while(GPIO.input(GPIO_RECEIVE) == GPIO.LOW):
			pass
		response = spi.readbytes(bytesToReceive)

		return str(response)


	#####################################################################
	#
	#	SEND A STRING VIA SPI
	#
	#	Provided a string, send entire string via SPI. Assumes
	#	micro knows data is coming.
	#
	#####################################################################

	def SendStringMessage(self, stringMessage):

		# Create list of int representation of string
		stringMessageAsInt = map(ord, list(stringMessage))

		# Set GPIO signal low to communicate message data being sent
		GPIO.output(GPIO_SENDMESSAGE, False)

		# Send message via spi
		while(len(stringMessageAsInt) > 0):
			stringMessageAsInt = self.SendBytes(stringMessageAsInt,
				SPI_DEFAULTSPEED)

		sleep(1)

		# Set GPIO signal back high
		GPIO.output(GPIO_SENDMESSAGE, True)

		# DELETE THIS SHIT
		sleep (1)
		GPIO.output(GPIO_SENDMESSAGE, False)


	#####################################################################
	#
	#	SEND A SONG VIA SPI
	#
	#	Provided the filepath of a song to play, method oversees the
	#	process of sending a song via SPI, implementing agreed protocol
	#	with Micro to know when to send more data (GPIO PIN). Sends at
	#	speed specified.
	#
	#####################################################################

	def SendSong(self, track, speed=SPI_DEFAULTSPEED):

		# Get preped song data
		bytes = track.Data

		# Fill buffer
		for init in range(SPI_BUFFERSIZE):
			bytes = self.SendBytes(bytes, speed)
		# Send data in chunks
		while(len(bytes) > 0):
			while(GPIO.input(GPIO_BUFFERFULL) == GPIO.LOW):
				pass
			bytes = self.SendBytes(bytes, speed)

	#####################################################################
	#
	#	SEND A SONG INFO TO BE DISPLAYED
	#
	#	Uses send string method to send the song info
	#
	#####################################################################

	def SendSongInfo(self, songTitle, songArtist=""):
		stringToSend = ""

		# Build strings to be displayed
		stringToSend += NOWPLAYING_HEADER
		stringToSend += NOWPLAYING_SONG + songTitle + '\n'
		stringToSend += NOWPLAYING_ARTIST + songArtist + '\n'
		stringToSend += NOWPLAYING_FOOTER

		# Send string
		self.SendStringMessage(stringToSend)
