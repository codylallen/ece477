#!/usr/bin/python
import audiotools
from CONSTANTS import *
import glob
import random
import re
import sys
import threading
from Track import *

class MusicDatabase:

	def __init__(self):
		self.Tracks = dict()

		songFilepathList = self.RetrieveSongListFromDirectoy()

		self.BuildDatabase(songFilepathList)

	#####################################################################
	#
	#	BUILD SONG DATABASE
	#
	#	Take in a list of files and populates the song database (dict)
	#	using Track objects
	#
	#####################################################################

	def BuildDatabase(self, songList):
		threads = []
		for songFilePath in songList:
		    t = threading.Thread(target=self.BuildWorker(songFilePath))
		    threads.append(t)
		    t.start()

    #####################################################################
	#
	#	THREAD WORKER FOR PROCESSING THE MUSIC
	#
	#	I don't believe this helps but hey, looks cool, yeah? Maybe
	#	because I'm using it wrong? Hmmm...
	#
	#####################################################################

	def BuildWorker(self, songFilePath):
		newTrackObject = Track(songFilePath)
		self.Tracks[newTrackObject.Title] = newTrackObject
		return

	#####################################################################
	#
	#	GET RANDOM SONG TITLE FROM THE DATABASE
	#
	#	Returns a random song title from the database. Used for when
	#		1. The user selects random start method or
	#		2. There are no votes in the database
	#
	#####################################################################

	def GetRandomSongTitle(self):
		# Get songs currently in database
		songTitles = self.GetSongsInDatabase()

		# Determine number of songs left in database
		numberOfSongs = len(songTitles)

		# Check for empty list or if only single song left
		if numberOfSongs == 0:
			return None
		elif numberOfSongs == 1:
			return songTitles[0]

		# Get random number (index)
		randomNumer = random.randint(0, numberOfSongs - 1)

		return songTitles[randomNumer]

	#####################################################################
	#
	#	GET SONG TITLES IN DATABASE
	#
	#	Returns the list of songs currently in the database
	#
	#####################################################################

	def GetSongsInDatabase(self):
		return self.Tracks.keys()

	#####################################################################
	#
	#	GET SONG TITLES IN DATABASE
	#
	#	Returns the list of songs currently in the database
	#
	#####################################################################

	def IsEmpty(self):
		return (len(self.GetSongsInDatabase()) == 0)

	#####################################################################
	#
	#	RETRIEVE SONGS IN DIRECTORY
	#
	#	Grabs a list of song files in the directory specified in the
	#	CONSTANTS file.
	#
	#####################################################################

	def RetrieveSongListFromDirectoy(self):
		targetFiles = MUSICDIRECTORY + "/*" + MUSICFILESTYPE

		# Get list of songs in directory path
		listOfFiles = glob.glob(targetFiles)

		return listOfFiles