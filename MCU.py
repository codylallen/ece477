#!/usr/bin/python
from constants import *
from DebugState import *

#####################################################################

def Main():
    print("Staring MCU . . .")

    debugState = DebugState()

    debugState.start()
    
    print("Exiting MCU. . .")

Main()
