#!/usr/bin/python

import sys

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

#####################################################################
#
#	WIFI CONFIGURATIONS
#
#####################################################################

# Wireless driver name
WIRELESS = 'wlan0'

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
PHP_CHOICETEMPLATE = "<p><input type=\"radio\" name=\"song\" value=\"TITLE\"/>TITLE</p>"

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
DEBUG = True

# Make webiste changes live vs dev (local)
VOTING_HOMEPAGE = VOTING_LIVE

# Preprocess Song Data
PREPROCESS = False