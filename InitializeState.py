#!/usr/bin/python
from CONSTANTS import *
from MusicDatabase import *
from Poll import *
from ResourceManager import *
from SPI import *
import sys
from Wifi import *

class InitializeState:

	def __init__(self, resourceManager):
		print("Starting Initialize State . . .")
		self.poll = resourceManager.poll
		self.spi = resourceManager.spi
		self.wifi = resourceManager.wifi
		self.musicDatabase = resourceManager.musicDatabase

	def start(self):

		# Populate ballet
		self.poll.PopulateBallet(self.musicDatabase.Tracks.keys())

		# Clear database
		self.poll.ClearDbTable()

		# Establish WiFi connection
		while(not self.EstablishWifiConnection()):
			pass

		while(True):
			pass
			# Send starting options
			# response = self.spi.SendMenu(STARTINGOPTIONS)

			# if (response == RANDOM):
				# Random method: pick random song
				# return self.pickRandomTrack()
			# else if (response == SPECIFIC):
				# Specific Option: Send song options
				# response = self.spi.SendMenu(self.musicDatabase.Tracks.keys())
				# return response
			# else:
				# self.SendMessage(ERRORMESSAGE)

	def EstablishWifiConnection(self):
		# Search for WiFi
		networks = self.wifi.ScanForNetworks()
		print(networks)
		# Send options to micro


		# Wait for response (timeout?)


		# Attempt connection (with failure procedure)
		#return status


