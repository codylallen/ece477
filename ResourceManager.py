#!/usr/bin/python
from CONSTANTS import *
from MusicDatabase import *
from Poll import *
from SPI import *
from Wifi import *
import sys

#####################################################################
#
#	RESOURCE MANAGER FOR ALL STATES
#
#	Acts as a resoruce wrapper for all helper components
#
#####################################################################

class ResourceManager:

	def __init__(self):
		self.poll = Poll()
		self.spi = SPI()
		self.wifi = Wifi()
		self.musicDatabase = MusicDatabase()
