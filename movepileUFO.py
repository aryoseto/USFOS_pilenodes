__author__ = 'aryo.seto'
__copyright__='Copyright 2017, The Lazy Project'
__version__ = "0.1.1"
__date__ = "3-Aug-2017"

"""
Script description:

To move back the piles above the mudline to their correct location.

            MovePile <control_file.inp>

                control_file.inp
                1st line -- ufo_source_file.fem
                2nd line -- number of nodes to be corrected [int]
                3rd line -- correction value to be added


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


# Function to read and write ufo file and adjusting the pile coordinates
def readwrite (target_name, source_name, number_of_nodes, correction_value):
    with open(target_name, 'w') as outfile:
        try:
            with open(source_name, 'r') as infile:
                counter = 0
                for line in infile:
                    if 'NODE ' in line and counter <= (number_of_nodes - 1):
                        # Counting how many nodes have been read
                        counter +=1
                        nodes = line.split()
                        # Correct the z coordinates
                        zcoord = float(nodes[4]) + correction_value
                        outfile.write('{: >5} {: >14} {: >14} {: >14} {: >14}'.format(nodes[0],nodes[1],nodes[2],nodes[3],str(zcoord)) + '\n')
                    else:
                        outfile.write(line)
            res = 1
        except:
            print('source file not found')
            res = 0
    return res


# ----- Execute Program ------

# Check if control file is given and valid
resargv = checkargv()

if resargv == 1:
    # echoing the name of the control file
    print('Reading control file: %s' % sys.argv[1])
else:
    # spit this when the control file not found, stop the program
    sys.exit('ERROR - Oops! Control file not found')


# Check if control file is giving the right parameter
# Obtaining list of parameters
ctrlpar = toList(sys.argv[1])

# Check if the source file exists
if os.path.exists(ctrlpar[0]):
    print('ufo source file : {} '.format(ctrlpar[0]) + 'found' )
else:
    print('{} not found! check your control file'.format(ctrlpar[0]))
    sys.exit('ERROR')


# Check the number of nodes given
if ctrlpar[1] == 0:
    sys.exit('ERROR - number of nodes cannot be 0')
else:
    try:
        int(ctrlpar[1])
        print('number of nodes to be adjusted : {}'.format(ctrlpar[1]))
    except:
        sys.exit('ERROR - number of nodes cannot be {}'.format(ctrlpar[1]))


# Check the adjustment value
if ctrlpar[2] == 0:
    sys.exit('ERROR - adjustment value cannot be 0')
else:
    try:
        float(ctrlpar[2])
        print('adjustment value : {}'.format(ctrlpar[2]))
    except:
        sys.exit('ERROR - adjustment value cannot be {}'.format(ctrlpar[2]))


# Obtaining parameters from control file
""" ctrlpar[0] --> ufo file source to be modified
    ctrlpar[1] --> number of nodes to be modified
    ctrlpar[2] --> z coordinate adjustment
"""

# Obtaining source file name
srcname = ctrlpar[0]

# Creating target file name
modname = ctrlpar[0][:-4] + "_MOD.FEM"

# Obtaining number of nodes to be adjusted
numberofnodes = int(ctrlpar[1])

# Obtaining z correction value
zcorrection = float(ctrlpar[2])


status = readwrite(modname, srcname, numberofnodes, zcorrection)

if status == 1:
    print('Normal Exit')
else:
    print('ERROR - produced file will not be correct')
