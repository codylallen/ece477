#!/usr/bin/python
from CONSTANTS import *
import glob
import MySQLdb
import re
import sys

class Poll:

	def __init__(self):

		# Estbalish connection to DB
		self.db = MySQLdb.connect(host=DB_HOST,
			user=DB_USER,
			passwd=DB_PASSWORD,
			db=DB_NAME)

		# Database currsor for executing
		self.cur = self.db.cursor()

	#####################################################################
	#
	#	ADD ONE SONG TO THE EXISITING POLL OPTIONS
	#
	#	Adds one song to the exisiting poll, injecting the choice
	#	into the index.php page
	#
	#####################################################################

	def AddSongToBallet(self, songTitle):
		if not songTitle:
			return

		targetForSongTitle = "TITLE"
		targetForNewChoice1 = ">\n"
		targetForNewChoice2 = "<input type=\"submit\" value=\"Submit\" />"
		targetForNewChoice = targetForNewChoice1 + ".*" + targetForNewChoice2
		LF = "\n"
		songTitle = songTitle


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
	#	CLEAR BALLET ON HOMEPAGE
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
	#	CLEAR ENTRIES IN SQL DB TABLE
	#
	#	Clears entries in the SQL DB table
	#
	#####################################################################

	def ClearDbTable(self):
		querey = "DELETE FROM " + DB_TABLE

		# SQL querey for song coloumn
		self.cur.execute(querey)

		# Commit changes
		self.db.commit()

	#####################################################################
	#
	#	DELETE TARGET ENTRIES IN SQL DB TABLE
	#
	#	Deletes a tarticular song entry from SQL DB given the name
	#
	#####################################################################

	def DeleteDbEntries(self, target):
		if not target:
			return

		querey = "DELETE FROM " + DB_TABLE + " WHERE song = '" + target + "'"

		# SQL querey for song coloumn
		self.cur.execute(querey)

		# Commit changes
		self.db.commit()

	#####################################################################
	#
	#	RETRIEVE VOTES FROM DATABASE
	#
	#	Returns list of votes from MySQL database
	#
	#####################################################################

	def GetDbData(self):
		querey = "SELECT song FROM " + DB_TABLE

		# SQL querey for song coloumn
		self.cur.execute(querey)

		# Collect song titles
		listOfSongs = []
		for row in self.cur.fetchall() :
			listOfSongs.append(row[0])

		return listOfSongs

	#####################################################################
	#
	#	OBTAIN TOP VOTED SONG
	#
	#	Returns the top voted item in the database
	#
	#####################################################################

	def GetDbTopSong(self):
		querey = "SELECT song FROM " + DB_TABLE + " GROUP BY song ORDER BY COUNT(*) DESC LIMIT 1";

		# SQL querey for song coloumn
		self.cur.execute(querey)

		# Extract song
		row = self.cur.fetchall()

		if not row:
			return None
		else:
			return row[0][0]

    #####################################################################
	#
	#	POPULATE POLL OPTIONS
	#
	#	Adds all songs pass to the method in a list, rewriting the
	#	existing options in index.php
	#
	#####################################################################

	def PopulateBallet(self):
		targetCleanSong = "(" + MUSICDIRECTORY + "/)(.*)(" + MUSICFILESTYPE + ")"
		targetGroup = 2
		targetFiles = MUSICDIRECTORY + "/*" + MUSICFILESTYPE

		# Get list of songs in directory path
		listOfFiles = glob.glob(targetFiles)

		# Clean list
		cleanList = []
		for song in listOfFiles:
			cleanSong = re.match(targetCleanSong, song)
			cleanList.append(cleanSong.group(targetGroup ))

		# Clean PHP file
		self.CleanBallet()

		# Write songs to list
		for song in cleanList:
			self.AddSongToBallet(song)

	#####################################################################
	#
	#	REMOVE ONE SONG FROM THE EXISITING POLL OPTIONS
	#
	#	Removes one song from the exisiting poll (index.php)
	#
	#####################################################################

	def RemoveSongFromBallet(self, songTitle):
		if not songTitle:
			return

		target = "<p>.*" + songTitle + "</p>\n"
		replacement = ""

		# Get current PHP file
		f = open(VOTING_HOMEPAGE, 'r')
		readLines = f.read()
		f.close()

		# Remove title
		newLines = re.sub(target, replacement, readLines)

		# Rewrite file
		f = open(VOTING_HOMEPAGE, 'w')
		f.write(newLines)
		f.close()
