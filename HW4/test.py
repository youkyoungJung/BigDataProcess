#!/usr/bin/python3
from numpy import *
from os import listdir
import operator

hwLabels = []
trainingFileList = listdir('./trainingDigits')
m = len(trainingFileList)
trainingMat = zeros((m, 1024))
for i in range(m):
	fileNameStr = trainingFileList[i]
	fileStr = fileNameStr.split('.')[0]
	classNumStr = int(fileStr.split('_')[0])
	print(fileStr)

