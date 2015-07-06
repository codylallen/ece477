#!/usr/bin/python
from wifi import Cell, Scheme
from CONSTANTS import *
import sys

class Wifi():

	def __init__(self):
		pass

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
	#	CONNECT TO WIFI NETWORK
	#
	#	Conects to a given wifi network, provided the name
	#
	#####################################################################

	def AttemptToConnectTo(self, targetName):
		# Find network cells in range
		cells = Cell.all(WIRELESS)

		# Find targetCell based on targetName
		for cell in cells:
			if (str(cell.ssid) == targetName):
				targetCell = cell

		# Check if cell retrieval failed
		if not targetCell:
			return False

		# Attempt Connection
		#try:
		scheme = Scheme.for_cell(WIRELESS, targetName, targetCell, "")
		#except TypeError:
		#	return False

		#try:
		scheme.save()
		#except IOError:
		#	return False

		scheme.activate()
		return True