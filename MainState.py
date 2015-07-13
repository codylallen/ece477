#!/usr/bin/python
from CONSTANTS import *
from MusicDatabase import *
from Poll import *
from ResourceManager import *
import sys
import time

class MainState:

	def __init__(self, resourceManager):
		print("Starting Main State . . .")
		self.poll = resourceManager.poll
		self.spi = resourceManager.spi
		self.wifi = resourceManager.wifi
		self.musicDatabase = resourceManager.musicDatabase

	def start(self, firstTrack):
		currentSong = firstTrack

		# Main Loop
		while not self.musicDatabase.IsEmpty():

			# Obtain track object from database
			currentTrack = self.musicDatabase.Tracks[currentSong]

			# Remove song option from website and votes form DB
			self.poll.RemoveSongFromBallet(currentSong)
			self.poll.DeleteDbEntries(currentSong)

			# Send song title/artist
			self.spi.SendSongInfo(currentSong, currentTrack.Artist)

			# Send song data
			self.spi.SendSong(currentTrack)

			# Remove song just played from database
			del self.musicDatabase.Tracks[currentSong]

			# Get next song to be played
			currentSong = self.poll.GetDbTopSong()

			if not currentSong:
				currentSong = self.musicDatabase.GetRandomSongTitle()


		# Closing procedure



