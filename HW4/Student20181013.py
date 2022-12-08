import numpy as np
import sys
from os import listdir
import operator

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
            key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]
    
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
for i in range(train_numberOfFiles):
	trainingMat[i, :] = fileToVector('./'+train_folder+'/%s'%train_file_names[i])
for i in range(test_numberOfFiles):
	testingMat[i, :] = fileToVector('./'+test_folder+'/%s'%test_file_names[i])
	
#값 확인
#test_Data = fileToVector('./'+test_folder+'/%s'%input("Input test file name: "))
#print(train_labels)

#result k에따라	
result = []
for i in range(1,21):
	classifyResult = []
	for j in range(test_numberOfFiles):			
		classifyResult.append(classify0(testingMat[j, :], trainingMat, train_labels, i))
	#print(i, classifyResult)
	result.append(classifyResult)
	#print("classify Result: %d " %classifyResult)
#print(result)	


#에러율계산
count = [0]*20
for i in range(20):
	for j in range(test_numberOfFiles):
		if result[i][j] != test_labels[j]:
			count[i] += 1
#print(count)

error_rate = [0]*20
for i in range(len(result)):		
	error_rate[i] = count[i] / len(result) * 100
	print("%.f"%error_rate[i])

#print("test_labels: ", test_labels)	
#print("result count: ", len(result))
#print("test_file_name:", test_file_names)




