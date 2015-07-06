#!/usr/bin/python
import audiotools
from CONSTANTS import *
import re
import sys

class Track:

	def __init__(self, filepath):

		self.Title = ""
		self.Artist = ""
		self.Data = []
		self.Filepath = filepath

		self.PopulateMetaData()

	#####################################################################
	#
	#	MANUALLY CREATES CLEAN TRACK TITLE
	#
	#	After Metadata extraction failure, fills in track title and
	#	artist name manually
	#
	#####################################################################

	def ManualMetaData(self):
		targetCleanSong = "(" + MUSICDIRECTORY + "/)(.*)(" + MUSICFILESTYPE + ")"
		targetGroup = 2

		cleanSong = re.match(targetCleanSong, self.Filepath)
		self.Title = cleanSong.group(targetGroup )


	#####################################################################
	#
	#	GATHERS TRACK DATA
	#
	#	Fills in track metadata using various methods. If metadata is in
	#	the song file itself, that data is extracted. Otherwise, manual
	#	methods are used.
	#
	#####################################################################

	def PopulateMetaData(self):
		audioFile = audiotools.open(self.Filepath)
		metaData = audioFile.get_metadata()

		if not metaData:
			self.ManualMetaData()
		else:
			self.Title = metaData.track_name
			self.Artist = metaData.artist_name

		if PREPROCESS:
			self.Data = self.PrepareSongData()

	#####################################################################
	#
	#	LOAD IN SONG DATA
	#
	#	Takes a file path and loads in the song data, preparing it for
	#	SPI transfer
	#
	#####################################################################

	def PrepareSongData(self):
		# Read in file
		f = open(self.Filepath, 'rb')
		bytes_read = f.read()
		f.close()

		# Convert read string to int representation
		bytes = []
		for byte in bytes_read:
			bytes.append(ord(byte))

		return bytes