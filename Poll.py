#!/usr/bin/python
from constants import *
import glob
import re
import sys

class Poll:

	def __init__(self):
		pass

	#####################################################################
	#
	#	ADD ONE SONG TO THE EXISITING POLL OPTIONS
	#
	#	Adds one song to the exisiting poll, injecting the choice
	#	into the index.php page
	#
	#####################################################################

	def AddSong(self, songTitle):
		targetForSongTitle = "TITLE"
		targetForNewChoice1 = ">\n"
		targetForNewChoice2 = "<input type=\"submit\" value=\"Submit\" />"
		targetForNewChoice = targetForNewChoice1 + targetForNewChoice2
		LF = "\n"


		# Get current PHP file
		f = open(VOTING_HOMEPAGE, 'r')
		readLines = f.read()
		f.close()

		# Create new line to add
		newLine = PHP_CHOICETEMPLATE
		newLine = re.sub(targetForSongTitle, songTitle, newLine)

		replacementForNewChoice = targetForNewChoice1 + newLine + LF + targetForNewChoice2

		# Insert title at location
		newLines = re.sub(targetForNewChoice, replacementForNewChoice, readLines)

		# Rewrite file
		f = open(VOTING_HOMEPAGE, 'w')
		f.write(newLines)
		f.close()

	#####################################################################
	#
	#	CLEARS BALLET ON HOMEPAGE
	#
	#	Clears and generates a clean index.php ballet for votinng
	#
	#####################################################################

	def CleanBallet(self):
		# Get clean PHP file
	    f = open(VOTING_CLEANPAGE, 'r')
	    homepageStructure = f.read()
	    f.close()

	    # Write clean structure
	    f = open(VOTING_HOMEPAGE, 'w')
	    f.write(homepageStructure)
	    f.close()

    #####################################################################
	#
	#	POPULATES POLL OPTIONS
	#
	#	Adds all songs pass to the method in a list, rewriting the
	#	existing options in index.php
	#
	#####################################################################

	def PopulateBallet(self, songDirectoryPath):

	    # Get list of songs in directory path
	    listOfFiles = glob.glob(songDirectoryPath + "/*.m4a")
	    print(listOfFiles)

	    # Clean list
	    cleanList = []
	    for song in listOfFiles:
	    	cleanSong = re.match("(" + songDirectoryPath + "/)(.*)(.m4a)", song)
	        cleanList.append(cleanSong.group(2))

	    # Clean PHP file
	    self.CleanBallet()

	    # Write songs to list
	    for song in cleanList:
	    	self.AddSong(song)
