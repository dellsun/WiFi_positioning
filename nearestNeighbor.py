"""
classification model based on K nearest neighbors.  The MS RADAR localization product also uses KNN
for their location predictions.  Basically, each vector within the design matrix is taken as a point in a
very high dimensional space and the Euclidean distance between the vector and the real-time data is computed.
Effective, the neighbors of the real-time data are voting for a particular location; most voted for location
is the prediction. 
"""


__project__ = 'DC2-localization'
__author__ = 'jcavalie'
__date__ = '5/8/14'
__email__ = 'Jcavalieri8619@gmail.com'


from sklearn.neighbors import KNeighborsClassifier
import numpy
from buildTestVectors import *

class KNNclassifier(object):
	_designMatrix=numpy.load('DesignMatrixBIN_.npy')
	_labelVector=numpy.load('LabelVectorBIN_.npy')
	
	def __init__(self, test=None):
		self._model=KNeighborsClassifier(n_neighbors=7,weights='distance')	
		self._model.fit(KNNclassifier._designMatrix,KNNclassifier._labelVector)
		if test is not None:
			self._testData=test
			
	def predictLocation(self,newData):
		return self._model.predict(newData)
	
	
def KNNmodelTester(arg=None):
	
	classifier=KNNclassifier()
	
	if arg is not None:
		p=classifier.predictLocation(arg)
		print 'Prediction: ',p
		print "Actual: 408"
	
	else:	
		for test in getTestingVectors():
			p=classifier.predictLocation(test[1])
			print "Prediction: ",p
			print "Actual: ",test[0]
		
	return

#KNNmodelTester()