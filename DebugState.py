#!/usr/bin/python
from CONSTANTS import *
from MusicDatabase import *
from Poll import *
from SPI import *
from Wifi import *
from ResourceManager import *
import sys

class DebugState:

	def __init__(self, resourceManager):
		print("Initializing Debug State . . .")
		self.poll = resourceManager.poll
		self.spi = resourceManager.spi
		self.wifi = resourceManager.wifi
		self.musicDatabase = resourceManager.musicDatabase

	def start(self):
		print("Starting Debug State . . .")
		if self.wifi.AttemptToConnectTo('TP-LINK_5B71BC'):
			print("Connection successful")
		else:
			print("Connection failed")




