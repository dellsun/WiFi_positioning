__project__ = 'DC2-localization'
__author__ = 'jcavalie'
__date__ = '5/5/14'
__email__ = 'Jcavalieri8619@gmail.com'

from buildDataVectors import *
from nearestNeighbor import KNNclassifier

def locator():
	
	the_model = KNNclassifier()
	try:
		dataMatrix=fetchRadioMaps()
	except Exception,msg:
		print msg
		return
	
	print "Current Location: ", the_model.predictLocation(dataMatrix)
	#outputs five results because we handed the model 5 radio maps to predict on
	
	return
	
	
locator()