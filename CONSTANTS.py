#!/usr/bin/python

import sys

#####################################################################
#
#	INITIALIZATION MENU RESPONSES
#
#####################################################################

# The prompt for starting options
STARTINGOPTIONS = "Please select starting method\nSelect SPECIFIC song\nRANDOM\n"

# Response indicating a random song should be picked to start
# 	NOTE: This may need to change based on establish communication
#			protocol. (i.e. may be changed to a number, etc.)
RANDOM = "RANDOM"

# Response indicating a specific song is to be selected to start
# 	NOTE: This may need to change based on establish communication
#			protocol. (i.e. may be changed to a number, etc.)
SPECIFIC = "Select SPECIFIC song"

# Error message when invalid response received
ERRORMESSAGE = "Selection error, please try again"


#####################################################################
#
#	SPI CONFIGURATIONS
#
#####################################################################

# SPI Max Block Size
SPI_MAXBLOCKSIZE = 4096

# Music buffer size
SPI_BUFFERSIZE = 4

# GPIO pin for bufferfull
GPIO_BUFFERFULL = 11

# GPIO pin for signaling text to be displayed
GPIO_SENDMESSAGE = 12

# GPIO pin for response ready on SPI
GPIO_RECEIVE = 13

# SPI default speed
SPI_DEFAULTSPEED = 5000

# SPI number of bytes to be received for menu response
MENURESPONSESIZE = 1

#####################################################################
#
#	WIFI CONFIGURATIONS
#
#####################################################################

# Wireless driver name
WIRELESS = 'wlan0'

# Wireless connection timeout
CONNECTIONTIMEOUT = 20

#####################################################################
#
#	POLL WEBSITE CONFIGURATIONS
#
#####################################################################

# Voting homepage options (SET BELOW)
VOTING_DEV = 'index.html'
VOTING_LIVE = '/var/www/index.html'

# Clean homepage path
VOTING_CLEANPAGE = "clean.html"

# Poll choice template in PHP syntax
PHP_CHOICETEMPLATE = "<p><input type=\"radio\" name=\"song\" value=\"CLEAN\"/>TITLE</p>"

#####################################################################
#
#	POLL DATABASE CONFIGURATIONS
#
#####################################################################

# SQL Database Information
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "DemoDJ2015"
DB_NAME = "learning"
DB_TABLE = "test3"

#####################################################################
#
#	MUSIC CONFIGURATIONS
#
#####################################################################

# Now Playing Framework / Template
NOWPLAYING_HEADER = "   DEMOCRATIC  DJ   \n"
NOWPLAYING_SONG = "Title: "
NOWPLAYING_ARTIST = "Artist: "
NOWPLAYING_FOOTER = "~~~~~~~~~~~~~~~~~~~~"

# Location of Music Files
MUSICDIRECTORY = "music"

# Supported file type
MUSICFILESTYPE = ".wav"

#####################################################################
#
#	DEBUG CONFIGURATIONS
#
#####################################################################

# Run Debug State
DEBUG = False

# Make webiste changes live vs dev (local)
VOTING_HOMEPAGE = VOTING_LIVE

# Preprocess Song Data
PREPROCESS = False