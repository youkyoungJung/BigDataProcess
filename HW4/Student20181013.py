import kNN
import numpy as np
import sys
from os import listdir
import operator

#디렉터리에서 파일이름으로 접근
def DirectoryToFileName(foldername):
	labels = []
	file_names = []
	file_list = listdir(foldername)
	#파일개수
	numberOfFiles = len(file_list)

	for line in range(numberOfFiles):
		fileNameStr = file_list[line]
		file_names.append(fileNameStr)
		
		fileStr = fileNameStr.split('.')[0]
		#데이터라벨값(0,1,2...)
		classNumStr = int(fileStr.split('_')[0])
		labels.append(classNumStr)
		
	return labels, file_names, numberOfFiles
	
#파일에서 read, make Vector
def fileToVector(filename):
    returnVec = np.zeros((1, 1024))
    f = open(filename)
    #numberOfLines = len(f.readlines())
    #print(numberOfLines)
    for i in range(32):
        lineStr = f.readline()
        #print(line)
        for j in range(32):
        	returnVec[0, 32*i+j] = int(lineStr[j])
        #classLabelVector.append(listFromLine[-1])
        #index += 1
    return returnVec#, classLabelVector
    	
#args인자받기
train_folder = sys.argv[1]
test_folder = sys.argv[2]

#train File data, name, numberOfFile
train_labels, train_file_names, train_numberOfFiles = DirectoryToFileName(train_folder)
#test File data, name, numberOfFile
test_labels, test_file_names, test_numberOfFiles = DirectoryToFileName(test_folder)

#print(train_file_names)
#data_Matrix
trainingMat = np.zeros((train_numberOfFiles, 1024))
testingMat = np.zeros((test_numberOfFiles, 1024))

#file read(contact data)	
for i in range(test_numberOfFiles):
	#with open('./'+train_folder+'/'+train_file_names[i], 'r') as f:
	trainingMat[i, :] = fileToVector('./'+train_folder+'/%s'%train_file_names[i])
	testingMat[i, :] = fileToVector('./'+test_folder+'/%s'%test_file_names[i])
		#print(train_file_names[i])	
#값 확인
#test_Data = fileToVector('./'+test_folder+'/%s'%input("Input test file name: "))
#print(train_labels)

#result 전체	
result = []
for i in range(test_numberOfFiles):	
	classifyResult = kNN.classify0(testingMat[i, :], trainingMat, train_labels, 3)
	result.append(classifyResult)
	print("classify Result: %d " %classifyResult)
	
print("result count: ", len(result))
		




