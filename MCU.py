#!/usr/bin/python
from CONSTANTS import *
from DebugState import *
from InitializeState import *
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
    	# Call Initalization State
    	initializeState = InitializeState(resourceManager)
    	firstTrack = initializeState.start()
        print(firstTrack)

    	# Call Main State
    	# Call main state with firstTrack


    print("\n\nExiting MCU. . .")

Main()
