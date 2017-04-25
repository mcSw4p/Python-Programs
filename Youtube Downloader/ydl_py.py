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

# Import pytube project
from pytube import YouTube

# Explanation
print("This script will download a youtube video from a URL.")

# YouTube variable
yt = YouTube(input("Enter Youtube URL: "))

# List all video quality options
count = 0
print("\n-- Quality Options --\n")
for X in yt.get_videos():
    print(count, X)
    count += 1

print()
# Ask user for a choice
choice = int(input("Enter Quality choice(-1 to skip): "))

# Select users choice of quality 
if choice != -1:
    count = 0
    for X in yt.get_videos():
        if count == choice:
            video = X
        count += 1
else:
    video = yt.get("mp4", "360p")

rename = input("Would you like to reanme the video file? (yes or no): ")

if rename == "yes":
    yt.set_filename(input("Enter new video title: "))

# Download video at users selected quality
video.download(input("\nEnter download path: "))

# Tell user that the fle has been downloaded
print("\nFinished Downloading (", yt.filename, ") ...")
    
