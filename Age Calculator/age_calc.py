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

print("This script will calculate how old you are in days, minutes and seconds.")
name = input("Name: ") # Ask for users name

print("Now please eneter your age.")
age = int(input("Age: ")) # Ask for users age

# Calculate Age in days, minutes, and seconds
days = age * 365 # Days
minutes = age * 525948 # Minutes
seconds = age * 31556926 # Seconds

# Print results to screen for user to read
print(name, "is", days, "days old,", minutes, "minutes old and", seconds, "seconds old!")
