#!/usr/bin/python
from CONSTANTS import *
from DebugState import *
from InitializeState import *
from MainState import *
from ResourceManager import *
import sys

#####################################################################

def Main():
    print("Staring MCU . . .\n\n")

    # Resource Wrapper to be passed to all states
    resourceManager = ResourceManager()

    if(DEBUG):
    	debugState = DebugState(resourceManager)
    	debugState.start()
    else:
    	while(true):
            # Call Initalization State
        	initializeState = InitializeState(resourceManager)
        	firstTrack = initializeState.start()

        	# Call Main State
        	mainState = MainState(resourceManager)
            status = mainState.start(firstTrack)

    print("\n\nExiting MCU. . .")

Main()
