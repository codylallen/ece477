#!/usr/bin/python
from wifi import Cell, Scheme
from CONSTANTS import *
import os
import signal
import sys

class Wifi():

	def __init__(self):
		pass

    #####################################################################
	#
	#	CONNECT TO WIFI NETWORK
	#
	#	Conects to a given wifi network, provided the name
	#
	#####################################################################

	def AttemptToConnectTo(self, targetName):
		targetCell = None

		# Find network cells in range
		cells = Cell.all(WIRELESS)

		# Find targetCell based on targetName
		for cell in cells:
			if (str(cell.ssid) == targetName):
				targetCell = cell

		# Check if cell retrieval failed
		if not targetCell:
			print("Failed to find chosen network")
			return False

		# Attempt Connection
		try:
			scheme = Scheme.for_cell(WIRELESS, targetName, targetCell)
		except TypeError:
			print("Failed to connect to scheme")
			return False

		try:
			scheme.save()
		except AssertionError:
			pass
		except IOError:
			print("Failed to save scheme")
			return False

		# Attempt to activate Scheme with timeout protection
		#signal.signal(signal.SIGALRM, TimeoutHandler)
		signal.alarm(CONNECTIONTIMEOUT)

		try:
			scheme.activate()
		except IOError:
			print("Activation of connection scheme timed out!")
			return False

		signal.alarm(0)

		# Successful connection
		return True

	#####################################################################
	#
	#	TIMEOUT PROTECTION HANDLER
	#
	#	Used to raise exception for timeout
	#
	#####################################################################

	def TimeoutHandler(signum, frame):
	    raise IOError


    #####################################################################
	#
	#	SCAN FOR WIFI NETWORKS
	#
	#	Scans for wifi networks and filters out duplicates, returns
	#	list of discovered networks as strings
	#
	#####################################################################

	def ScanForNetworks(self):
	    cells = Cell.all(WIRELESS)
	    listOfCells = []
	    for cell in cells:
	        if str(cell.ssid) not in listOfCells:
	            listOfCells.append(str(cell.ssid))
	    return(listOfCells)



    #####################################################################
	#
	#	I don't understand why, but this must be outside of function?
	#	V	V	V	V	V	V	V	V	V	V	V	V	V	V	V	V
	#####################################################################

	signal.signal(signal.SIGALRM, TimeoutHandler)

