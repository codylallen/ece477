#!/usr/bin/python
from CONSTANTS import *
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

		#self.poll.CleanBallet()
		#self.poll.PopulateBallet()

		song = self.poll.GetDbTopSong()
		print("Top song is " + song)
		self.poll.RemoveSongFromBallet(song)
		self.poll.DeleteDbEntries(song)




