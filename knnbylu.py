from numpy import *
from scipy.spatial import distance
import operator
import numpy
def createDataSet():
	group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels=['A','A','B','B']
	return group,labels
def classify(inx,dataSet,labels,k):
	dd={}
	for i in range(len(dataSet)):
		dis=distance.euclidean(inx,dataSet[i])
		dd[i]=dis
	ddic=sorted(dd.iteritems(),key=lambda d:d[1])
	ll={}
	for j in range(k):
		index=ddic[j][0]
		label=labels[index]
		if label in ll:
			ll[label]=ll[label]+1
		else:
			ll[label]=1
	llsort=sorted(ll.iteritems(),key=lambda d:d[1],reverse=True)
	return llsort[0][0]
def file2matrix(filename):
	fr=open(filename)
	lines=fr.readlines()
	rawdata=zeros((len(lines),3))
	classlabel=[]
	index=0
	for line in lines:
		line=line.strip()
		listfromline=line.split('\t')
		rawdata[index,:]=listfromline[:3]
		if listfromline[-1]=='largeDoses':
			classlabel.append(2)
		if listfromline[-1]=='smallDoses':
			classlabel.append(1)
		if listfromline[-1]=='didntLike':
			classlabel.append(0)
		index+=1
	fr.close()
	return rawdata,classlabel
def autoNorm(dataSet):
    min=dataSet.min(0)
    max=dataSet.max(0)
    [m,n]=dataSet.shape
    data=numpy.zeros([m,n])
    data=(dataSet-tile(min,(m,1)))/(tile(max-min,(m,1)))
    return data




























