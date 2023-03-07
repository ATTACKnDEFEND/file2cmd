import base64
import os
import sys

# Set the chunk size
chunk_size = 500

# Set the output files
joined_file = "joined.txt"
output_file = "spacerun.jpg"

# Check if the file name is provided as an argument
if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Open the input file and read its contents
with open(filename, "rb") as f:
    file_contents = f.read()

# Convert the file contents to base64
base64_contents = base64.b64encode(file_contents).decode()


# Create the output file and write the echo statements
with open(filename + ".cmd", "w") as f:
    f.write("@echo off\n")
    f.write("setlocal EnableDelayedExpansion\n")
    f.write("set joined=" + joined_file + "\n")
    f.write("set output=" + output_file + "\n")
    f.write("echo " + base64_contents[:chunk_size] + " > !joined!\n")

    # Write the remaining echo statements
    base64_contents = base64_contents[chunk_size:]
    while len(base64_contents) > 0:
        f.write("echo " + base64_contents[:chunk_size] + " >> !joined!\n")
        base64_contents = base64_contents[chunk_size:]

    # Add the certutil command to decode the output file
    f.write("certutil -f -decode !joined! !output!")