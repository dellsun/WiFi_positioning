"""
Constructs the design matrix containing 3054 rows and 820 columns. The rows represent each radio map
that was built by visiting each room on the fourth floor Olsen and walking around in room in various paths.
The columns represent the features of the radio map - namely MAC address and signal strength. Evert two
consecutive positions represent whether the AP was sensed during the construction of the current radio map
and if it was then its signal strength is added.  
"""
__author__ = 'jcavalie'

import numpy
import scipy
import os



def buildDesignMatrix( ):
	designMatrix = numpy.zeros( (3052,820), order = 'C' )
	labelVect=numpy.empty((0,0),dtype=int)
	fileCount = 0
	roomNumbers = [ '03', '04', '05', '06', '07', '08', '10', '12' ]

	for num in roomNumbers:

		dirprefix='/home/jcavalie/PycharmProjects/DC2-localization/DATA/radioMaps.formatted/'
		radioMap_files = os.listdir( dirprefix+'R4'+num  )
				

		for currCount, currfile in enumerate( radioMap_files ):

			currRadioMap = numpy.loadtxt( dirprefix+currfile, usecols = (0, 1),dtype=('i4,f4') )
						
			for value in  numpy.nditer( currRadioMap ):
				
				APid=2*(value.tolist()[0])
				SignalStrength=value.tolist()[1]
				
				designMatrix[currCount+fileCount][ APid ] = 1
				designMatrix[currCount+fileCount][ APid+1 ] = SignalStrength
				
			
		fileCount += len(radioMap_files)
		tempLabelVect=numpy.ndarray((len(radioMap_files),1))
		tempLabelVect.fill(int(num)+400)
		labelVect=numpy.append(labelVect,tempLabelVect)
	
	#save files to disk so that they needn't be recomputed each run	
	numpy.save('DesignMatrixBin_',designMatrix)
	numpy.save('LabelVectorBIN_',labelVect)
	
	return
	
buildDesignMatrix()


			
			
					