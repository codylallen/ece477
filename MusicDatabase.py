#!/usr/bin/python
import audiotools
from CONSTANTS import *
import glob
import re
import sys
from Track import *

class MusicDatabase:

	def __init__(self):
		self.Tracks = dict()

		songFilepathList = self.RetrieveSongListFromDirectoy()

		self.BuildDatabase(songFilepathList)


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

	#####################################################################
	#
	#	BUILD SONG DATABASE
	#
	#	Take in a list of files and populates the song database (dict)
	#	using Track objects
	#
	#####################################################################

	def BuildDatabase(self, songList):

		for songFilePath in songList:
			newTrackObject = Track(songFilePath)
			self.Tracks[newTrackObject.Title] = newTrackObject

