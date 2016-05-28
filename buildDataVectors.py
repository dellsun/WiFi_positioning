"""
fetches raw radio maps output by the Locator script.  Each radio map is converted into a small design 
matrix and handed off the model to predict current location.
"""

__project__ = 'DC2-localization'
__author__ = 'jcavalie'
__date__ = '5/5/14'
__email__ = 'Jcavalieri8619@gmail.com'

import cPickle
import os
import numpy

def fetchRadioMaps():
	

	with open('BSSmappings.pickle','rb') as file:
		BSSmappings=cPickle.load(file)
		
	#location of radio maps used for real time localization	
		
	radioMap_files = os.listdir( './DATA/realtimeData/' )
	
	if len(radioMap_files) == 0:
		raise Exception("Error: realtime data folder empty")
	
	##mobile station will collect 5 radio maps
	dataMatrix= numpy.zeros( (5,820), order = 'C' )
	
	for currCount,currfile in enumerate(radioMap_files):
		
	
		convertBSS=lambda BSSstr: BSSmappings.get(BSSstr,-1)
		
		currRadioMap=numpy.loadtxt('./DATA/realtimeData/'+currfile,dtype=('i4,f4'),converters={0:convertBSS },
		                           usecols=(0,3,))
		
		#remove file so that next execution will have real time data only
		os.remove('./DATA/realtimeData/'+currfile)
		for value in  numpy.nditer( currRadioMap ):
				
				if value.tolist()[0] == -1:
					print "Unknown AP, disregarding for now"
					continue
				
				APid=2*(value.tolist()[0])
				SignalStrength=value.tolist()[1]
				
					#if unknown AP found, just disregard
				
				dataMatrix[currCount][ APid ] = 1
				dataMatrix[currCount][ APid+1 ] = SignalStrength
		
	
	return dataMatrix

	
	
	
	