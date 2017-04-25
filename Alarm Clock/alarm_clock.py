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
import webbrowser
import random
import os

# Global variables
elsewhere = False
filename = "videos.txt"

timeformat = "%H:%M"

# Check to see if the videos file exists
if os.path.isfile(filename) == False:
    print("I cannot find the videos file!")
    choice = input("Enter the path to the file or nothing to create a new one: ") # Ask for file location

    # Create new file if choice is empty  
    if choice == "":
        flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
        filecreate = os.open(filename, flags)
        with os.fdopen(filecreate, 'w') as fileCreated:
            fileCreated.write("https://www.youtube.com/watch?v=FX7MSDySYkY")
    else:
        elsewhere = True
        

# Ask user what time they waht to me woke up
print("What time do you want to wake up? (ex. 09:30)")
Alarm = input("> ")

# Get current time
Time = time.strftime(timeformat)

if elsewhere == True:
    filename = choice 

# Open file and read URL's 
with open(filename) as f:
    content = f.readlines()

# Loop until the current time equals the alarm
while Time != Alarm:
    Time = time.strftime(timeformat) # Reset current time
    time.sleep(30) # Sleep for a 30 seconds

    # Check if current time equals alarm
    if Time == Alarm:
	print("Time to Wake up!")
	random_video = random.choice(content) # Pick a random video from file list
	webbrowser.open(random_video) # Open random file in default web browser
