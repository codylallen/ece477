#!/usr/bin/python

import sys

# SPI Max Block Size
SPI_MAXBLOCKSIZE = 4096

# Music buffer size
SPI_BUFFERSIZE = 4

# GPIO pin for bufferfull
GPIO_BUFFERFULL = 11

# Wireless driver name
WIRELESS = 'wlan0'

# Voting homepage options (SET BELOW)
VOTING_DEV = 'index.php'
VOTING_LIVE = '/var/www/index.php'

# Clean homepage path
VOTING_CLEANPAGE = "clean.php"

# Make changes live vs dev
VOTING_HOMEPAGE = VOTING_DEV

# Poll choice template in PHP syntax
PHP_CHOICETEMPLATE = "<p><input type=\"radio\" name=\"song\" value=\"TITLE\"/>TITLE</p>"

# SQL Database Information
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "DemoDJ2015"
DB_NAME = "learning"
DB_TABLE = "test3"

