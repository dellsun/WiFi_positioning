"""
BSStoInt: The MAC address of each unique access point encountered during radio map construction period
is mapped to a unique integer; an AP ID. This make computation and graphing easier. The dictionary BSSmappings
is then stored to disk so that during real time operation, the mappings can just loaded from disk instead of
recomputed.
"""

__author__ = 'jcavalie'

import numpy
import os
import cPickle

BSSmappings = { }


def mapBSStoInt( ):
	global BSSmappings

	roomNumbers = [ '03', '04', '05', '06', '07', '08', '10', '12' ]

	for num in roomNumbers:

		
		radioMap_files = os.listdir('./DATA/radioMaps.orig.noempty/R4' + num )

		for currfile in radioMap_files:

			currRadioMap = numpy.loadtxt( currfile, dtype = str, usecols = (0,) )

			for BSS in currRadioMap:
				BSSmappings.setdefault( BSS, len( BSSmappings ) )

			
			#convertBSS=lambda BSSstr: str(BSSmappings.get(BSSstr))
			#for currfile in radioMap_files:
			#	radioMap=numpy.loadtxt(currfile,dtype=str,converters={0:convertBSS },usecols=(0,3,4,))
			#   numpy.savetxt(currfile.replace('.txt','.dat'),radioMap,fmt=["%-s", "%-s","%-s"])


	return


#mapBSStoInt( )
		
		
		