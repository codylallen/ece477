#!/usr/bin/python
from constants import *
from Poll import *
from SPI import *
from Wifi import *
import sys

class DebugState:

	def __init__(self):
		print("Initializing Debug State . . .")
		self.poll = Poll()
		self.spi = SPI()
		self.wifi = Wifi()

	def start(self):
		print("Starting Debug State . . .")
		self.spi.SendSong("Shake It Off.wav", 45000)


