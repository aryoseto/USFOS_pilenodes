__author__ = 'aryo.seto'
__copyright__='Copyright 2017, The Lazy Project'
__version__ = "0.1.0"
__date__ = "28-July-2017"

"""
Script description:

To move back the piles above the mudline to their correct location.

            CombSub <control_file.inp>

Next development:
1. Put proper logger --> produce log file, instead of using "print"
2. Put help feature
3. Autorship print at the end of the run

test git in this file!!

"""

import os
import sys


# # Function for checking argument
# def checkargv():
#     res = 0
#     if len(sys.argv) == 1:
#         print('Please input the control file name with its extension')
#     elif len(sys.argv) > 2:
#         print('Only accept 1 argument')
#     elif len(sys.argv) == 2:
#         if os.path.exists(sys.argv[1]):  # check whether the path is valid
#             res = 1
#         else:
#             print('Path is not valid!')
#     return res
#
# # Function to read lines into a list
# def toList(nameoffile):
#     with open(nameoffile, 'r') as f:
#         llist = [line.strip() for line in f]
#     return llist


pile_nodes = []

#with open('K8F320T1_ufo_mod.FEM', 'w') as outfile:
#    with open('K8F320T1_ufo.FEM', 'w') as infile:
#        for line in infile:
#            if 'NODE' in line:
#                counter = 1
#                pile_nodes.append(line)

counter = 0
# identify the pile node lines
with open('K8F320T1_ufo_MOD.FEM', 'w') as outfile:
    with open('K8F320T1_ufo.FEM', 'r') as infile:
        for line in infile:
            if 'NODE ' in line and counter <= 10 :
                counter += 1
                #pile_nodes.append(line)
                nodes = line.split()
                



                #print(line)

#print('\n'.join(pile_nodes))
#print(*pile_nodes)

#splitting each column
def line_to_list (listtosplit):
    splittedline = []
    splittedlist = []
    for line in listtosplit:
        splittedline = line.split()
        splittedlist.append(splittedline)
    return splittedlist

pile_nodes_list = line_to_list(pile_nodes)

#print(*pile_nodes_list, sep='\n')

print(pile_nodes_list[0])

print(type(pile_nodes[4]))






