
# Getting full or absolute path of the current directory
#
# Algorithm:
# Copy this Py file into the needed folder -->
# --> Open Terminal window (or Anaconda Prompt) and activate Python v3 environment -->
# --> Go inside needed folder by command(s): 'cd' -->
# --> Launch this Py file by command:
#     'python3 getting-full-path.py'
#     or
#     'python getting-full-path.py'
# --> Copy received full path
#
# Result:
# Full or absolute path to the current folder in which this file was run


# Importing needed library
import os

# Getting full path of the current directory
# By using 'os.path.dirname(os.path.abspath(__file__))'
# we get full path to the directory in which this file is stored
current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)
