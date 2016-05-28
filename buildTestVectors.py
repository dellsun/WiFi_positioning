"""
fetches test radio maps so that accuracy of model can be determined; for my sample test set the accuracy is
100%.  Of course, if the user is in a hallway on fourth floor or in R401 then the system will output 
a best guess; probably R402. (R401 had a class when I was collecting data so I was unable to get its radio map)
"""

__project__ = 'DC2-localization'
__author__ = 'jcavalie'
__date__ = '5/9/14'
__email__ = 'Jcavalieri8619@gmail.com'

import os
import numpy



def getTestingVectors():
	
	dirprefix='./DATA/test_data/' 
	radioMap_files = os.listdir(dirprefix  )

	
	for currCount,currfile in enumerate(radioMap_files):


		testVector = numpy.zeros( (1, 820), order = 'C' )
		currRadioMap = numpy.loadtxt( dirprefix+currfile, usecols = (0, 1),dtype=('i4,f4') )
			
		for value in  numpy.nditer( currRadioMap ):
				
				APid=2*(value.tolist()[0])
				SignalStrength=value.tolist()[1]
				if SignalStrength is None:
					continue
					#if unknown AP found, just disregard
				
				testVector[0][ APid ] = 1
				testVector[0][ APid+1 ] = SignalStrength
		
		yield (radioMap_files[currCount],testVector)
		