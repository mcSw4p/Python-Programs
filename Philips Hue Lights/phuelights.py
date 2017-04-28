'''
 * Copyright (C) 2017  Sw4p
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * 
 * @author Sw4p
 *
'''

import time
from time import sleep

# This project uses the library phue located here(https://github.com/studioimaginaire/phue)
from phue import Bridge

# Ask user for the ip address for the bridge
print("Please enter the IP address of your Philips Hue Bridge: ")
bridge_ip = input(">> ")   

# Logic
def doWork():
    # Tell user they have connected to the bridge
    print("You have connected to the Bridge!\n")

    # List lights and id's
    print("Here is a list of lights:")
    for l in b.get_light_objects('id'):
        print("  - " + str(l) + ":" + b.get_light_objects('id')[l].name)

    # List groups and id's
    print("\nHere is a list of groups:")
    for g in b.get_group():
        print("  - " + g + ":" + b.get_group(int(g), 'name'))
        for li in b.get_group(int(g), 'lights'):
            print("\t+ " + b.get_light(int(li), 'name'))
    
    # Set running variable
    running = True

    # Loop until user enters 'exit'
    while running:
        # Ask what the user would like to do
        print("\nWhat would you like to do? (\'help\' for help)")
        command = input(">> ")

        # Split command into list
        command = command.split()
        
        if command[0] == "exit":
            # Exit script
            running = False;
        elif command[0] == "group":
            if len(command) >= 3:
                if command[2] == "on":
                    if len(command) == 4:
                        # Set Transition Time to inputted value and brightness to 0 for all lights in group 
                        for li in b.get_group(int(command[1]), 'lights'):
                            put = {'transitiontime' : int(command[3]) * int("10"), 'on' : True, 'bri' : 254}
                            b.set_light(int(li), put)
                    elif len(command) == 5:
                        # Set Transition Time to inputted value and brightness to inputted value for all lights in group
                        for li in b.get_group(int(command[1]), 'lights'):
                            put = {'transitiontime' : int(command[3]) * int("10"), 'on' : True, 'bri' : int(command[4])}
                            b.set_light(int(li), put)
                    else:
                        # Turn all lights in group on
                        for li in b.get_group(int(command[1]), 'lights'):
                            put = {'on' : True, 'bri' : 254}
                            b.set_light(int(li), put)
                elif command[2] == "off":
                    if len(command) == 4:
                        # Set Transition Time to inputted value and brightness to 0 for all lights in group 
                        for li in b.get_group(int(command[1]), 'lights'):
                            put = {'transitiontime' : int(command[3]) * int("10"), 'on' : False, 'bri' : 0}
                            b.set_light(int(li), put)
                    elif len(command) == 5:
                        # Set Transition Time to inputted value and brightness to inputted value for all lights in group
                        for li in b.get_group(int(command[1]), 'lights'):
                            put = {'transitiontime' : int(command[3]) * int("10"), 'on' : False, 'bri' : int(command[4])}
                            b.set_light(int(li), put)
                    else:
                        # Turn all lights in group off
                        for li in b.get_group(int(command[1]), 'lights'):
                            put = {'on' : False, 'bri' : 0}
                            b.set_light(int(li), put)
            else:
                print("Usage: group [id] [on|off] (transition time) (brightness)") # Error  
        elif command[0] == "light":
            if len(command) >= 3:
                if command[2] == "on":
                    if len(command) == 4:
                        # Set Transition Time to inputted value and brightness to 0
                        put = {'transitiontime' : int(command[3]) * int("10"), 'on' : True, 'bri' : 254}
                        b.set_light(int(command[1]), put)
                    elif len(command) == 5:
                        # Set Transition Time to inputted value and bright to inputted value
                        put = {'transitiontime' : int(command[3]) * int("10"), 'on' : True, 'bri' : int(command[4])}
                        b.set_light(int(command[1]), put)
                    else:
                        # Turn light on
                        put = {'on' : True, 'bri' : 254}
                        b.set_light(int(command[1]), put)
                elif command[2] == "off":
                    if len(command) == 4:
                        # Set Transition Time to inputted value and brightness to 0
                        put = {'transitiontime' : int(command[3]) * int("10"), 'bri' : 0}
                        b.set_light(int(command[1]), put)
                    elif len(command) == 5:
                        # Set Transition Time to inputted value and bright to inputted value
                        put = {'transitiontime' : int(command[3]) * int("10"), 'bri' : int(command[4])}
                        b.set_light(int(command[1]), put)
                    else:
                        # Turn light off
                        put = {'on' : False, 'bri' : 0}
                        b.set_light(int(command[1]), put)
            else:
                print("Usage: light [id] [on|off] (transition time) (brightness)") # Error
        elif command[0] == "help":
            # Print help page
            print("\nHelp page:\n")
            print("  - light [id] [on|off] (transition time) (brightness)")
            print("  - group [id] [on|off] (transition time) (brightness)")
            print("  - list [group|light]")
            print("  - help | Display help page")
            print("  - exit | exit script")
        elif command[0] == "list":
            if len(command) == 2:
                if command[1] == "light":
                    # List all lights and their id's
                    print("\nHere is a list of lights:")
                    for l in b.get_light_objects('id'):
                        print("  - " + str(l) + ":" + b.get_light_objects('id')[l].name)
                elif command[1] == "group":
                    # List all groups and their id's
                    print("\nHere is a list of groups:")
                    for g in b.get_group():
                        print("  - " + g + ":" + b.get_group(int(g), 'name'))
                        for li in b.get_group(int(g), 'lights'):
                            print("\t+ " + b.get_light(int(li), 'name'))
                else:
                    print("Usage: list [group|light]") # Error
            else:
                print("Usage: list [group|light]") # Error
        else:
            print("Unknown command.") # Error

# Starting Connection
try:
    # Try to connect to bridge
    b = Bridge(bridge_ip)
except:
    # Ask user to press link button on bridge
    print("Go press the link button on your bridge within 30sec:")

    # Sleep for 30 seconds
    time.sleep(30)

    # Try again
    try:
        b = Bridge(bridge_ip)    
    except:
        print("You did not press the link button!") # Error
    doWork() # Working method
doWork() # Working method
