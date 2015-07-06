#!/usr/bin/python
from CONSTANTS import *
from Poll import *
from SPI import *
from Wifi import *
import sys

class InitializeState:

	def __init__(self):
		print("Starting Initialize State . . .")
		self.poll = Poll()
		self.spi = SPI()
		self.wifi = Wifi()

	def start(self):
		# Populate ballet

		# Clear database

		# Search for WiFi

		# Send options to micro

		# Wait for response (timeout?)

		# Attempt connection (with failure procedure)

		# Send starting options

		# Random method: pick random song and call MainState

		# Specific Option: Send song options

		# Specific Option: Wait for reponse

		# Specific Option: Store selected song and call MainState



