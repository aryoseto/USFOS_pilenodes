__author__ = 'aryo.seto'
__copyright__='Copyright 2017, The Lazy Project'
__version__ = "0.1.0"
__date__ = "3-Aug-2017"

"""
Script description:

To move back the piles above the mudline to their correct location.

            MovePile <control_file.inp>

                control_file.inp
                1st line -- ufo_source_file.fem
                2nd line -- number of nodes to be corrected [int]


Next development:
1. Put proper logger --> produce log file, instead of using "print"
2. Put help feature
3. Autorship print at the end of the run


"""

import os
import sys


# Function for checking argument
def checkargv():
    res = 0
    if len(sys.argv) == 1:
        print('Please input the control file name with its extension')
    elif len(sys.argv) > 2:
        print('Only accept 1 argument')
    elif len(sys.argv) == 2:
        if os.path.exists(sys.argv[1]):  # check whether the path is valid
            res = 1
        else:
            print('Path is not valid!')
    return res


# Function to read lines into a list
def toList(nameoffile):
    with open(nameoffile, 'r') as f:
        llist = [line.strip() for line in f]
    return llist


# ----- Execute Program ------
resargv = checkargv()

if resargv == 1:
    # echoing the name of the control file
    print('Reading control file: %s' % sys.argv[1])
    OpenFileName = sys.argv[1]
else:
    # spit this when the control file not found, stop the program
    sys.exit('ERROR - Oops! Control file not found')


# Obtaining parameters from control file
""" ctrlpar[0] --> ufo file source to be modified
    ctrlpar[1] --> number of nodes to be modified
    ctrlpar[2] --> z coordinate adjustment
"""
# Obtaining list of parameters
ctrlpar = toList(sys.argv[1])

# Obtaining source file name
srcname = ctrlpar[0]

# Creating target file name
modname = ctrlpar[0][:-4] + "_MOD.FEM"

# Obtaining number of nodes to be adjusted
numberofnodes = int(ctrlpar[1])

# Obtaining z correction value
zcorrection = float(ctrlpar[2])

# identify the pile node lines and correcting the z coordinate
with open(modname, 'w') as outfile:
    with open(srcname, 'r') as infile:
        counter = 0
        for line in infile:
            if 'NODE ' in line and counter <= (numberofnodes - 1):
                # Checking how many nodes has been read
                counter += 1
                nodes = line.split()
                # Correct the z coordinates
                zcoord = float(nodes[4]) + zcorrection
                outfile.write(' ' + nodes[0] + '         ' + nodes[1] + '   ' + nodes[2] + '   ' + nodes[3] + '   ' + str(zcoord) + '\n')
            else:
                outfile.write(line)
