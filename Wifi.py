#!/usr/bin/python
from wifi import Cell, Scheme
from constants import *
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

	def scanForNetworks(self):
	    cells = Cell.all(WIRELESS)
	    listOfCells = []
	    for cell in cells:
	        if str(cell.ssid) not in listOfCells:
	            listOfCells.append(str(cell.ssid))
	    return(listOfCells)