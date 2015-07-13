#!/usr/bin/python
from CONSTANTS import *
from MusicDatabase import *
from Poll import *
from ResourceManager import *
import sys

class InitializeState:

	def __init__(self, resourceManager):
		print("Starting Initialize State . . .")
		self.poll = resourceManager.poll
		self.spi = resourceManager.spi
		self.wifi = resourceManager.wifi
		self.musicDatabase = resourceManager.musicDatabase

	def start(self):
		songsInDatabase = list()

		# Populate ballet
		songsInDatabase = self.musicDatabase.GetSongsInDatabase()
		self.poll.PopulateBallet(songsInDatabase)

		# Clear database
		self.poll.ClearDbTable()

		# Establish WiFi connection
		# <!-- ASSUMING WIFI CONNECTION -->
		#while(not self.EstablishWifiConnection()):
		#	pass

		while(True):
			response = None
			songChoice = None

			# Send starting options
			while not response:
				response = self.spi.SendMenuChoices(STARTINGOPTIONS)

			if (response == RANDOM):
			 	return self.musicDatabase.GetRandomSongTitle()

			elif (response == SPECIFIC):
				songChoice = self.spi.SendMenuChoices(songsInDatabase)
				if songChoice in songsInDatabase:
					return songChoice

			self.spi.SendStringMessage(ERRORMESSAGE)

	def EstablishWifiConnection(self):
		# Search for WiFi
		networks = self.wifi.ScanForNetworks()
		print(networks)
		# Send options to micro


		# Wait for response (timeout?)


		# Attempt connection (with failure procedure)
		# return self.wifi.AttemptToConnectTo(name)


