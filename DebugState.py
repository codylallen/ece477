#!/usr/bin/python
from CONSTANTS import *
from InitializeState import *
from MusicDatabase import *
from Poll import *
from ResourceManager import *
from SPI import *
import sys
from Wifi import *

class DebugState:

	def __init__(self, resourceManager):
		print("Initializing Debug State . . .")
		self.poll = resourceManager.poll
		self.spi = resourceManager.spi
		self.wifi = resourceManager.wifi
		self.musicDatabase = resourceManager.musicDatabase
		self.resourceManager = resourceManager

	def start(self):
		print("Starting Debug State . . .")
		#self.spi.SendMenuChoices("Testing\nHey\nChris\nIt's working!")
		#self.spi.SendSongInfo("Test Track", "Cody Allen")
		initializeState = InitializeState(self.resourceManager)
		firstTrack = initializeState.start()
		print(firstTrack)




