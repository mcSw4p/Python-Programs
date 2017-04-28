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

import argparse
import base64

# Create arg parser
parser = argparse.ArgumentParser(description='Decode a file or string or text')

# Add Type argument
parser.add_argument('-type', help='URLBase64, Base64, Base32, Base16 (u64,64,32,16)', default="64")

# Add Source argument
parser.add_argument('-source', help='Text to decode', nargs='+')

# Set args
args = parser.parse_args()

# If codetype is Base64
if args.type == "64":
    print(base64.decodestring(bytes(" ".join(str(x) for x in args.source), "utf-8")).decode())
# If codetype is Base32
elif args.type == "32":
    print(base64.b32decode(bytes(" ".join(str(x) for x in args.source), "utf-8")).decode())
# If codetype is Base16
elif args.type == "16":
    print(base64.b16decode(bytes(" ".join(str(x) for x in args.source), "utf-8")).decode())
# If codetype is URL safe Base64
elif args.type == "u64":
    print(base64.urlsafe_b64decode(bytes(" ".join(str(x) for x in args.source), "utf-8")).decode())
# If codetype is anythong else
else:
    print("Type has to be 64/32/16/u64.") # Error
