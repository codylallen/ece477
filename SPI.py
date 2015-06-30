#!/usr/bin/python
from constants import *
import RPi.GPIO as GPIO
import spidev
import sys

class SPI():

	def __init__(self):
		self.spi = spidev.SpiDev()
		self.spi.open(0,0)

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
	#	SEND A SONG VIA SPI
	#
	#	Provided the filepath of a song to play, method oversees the
	#	process of sending a song via SPI, implementing agreed protocol
	#	with Micro to know when to send more data (GPIO PIN). Sends at
	#	speed specified.
	#
	#####################################################################

	def SendSong(self, filepath, speed):

		# Get preped song data
		bytes = self.PrepareSongData(filepath)

		# GPIO setup
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		GPIO.setup(GPIO_BUFFERFULL, GPIO.IN)

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
	#	LOAD IN SONG DATA
	#
	#	Takes a file path and loads in the song data, preparing it for
	#	SPI transfer
	#
	#####################################################################

	def PrepareSongData(self, filepath):
		# Read in file
		f = open(filepath, 'rb')
		bytes_read = f.read()
		f.close()

		# Convert read string to int representation
		bytes = []
		for byte in bytes_read:
			bytes.append(ord(byte))

		return bytes



