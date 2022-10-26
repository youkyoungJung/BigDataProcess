#!/usr/bin/python3
import sys

#print(sys.argv[1])
genre = []
genres = dict()

try:
	with open(sys.argv[1], "rt") as f:
		
		for line in f:
			str_arr = line.split("::")
			str_arr2 = str_arr[2].split("|")
			
			for i in str_arr2:
				genre.append(i.strip())
			#genre.append(str_arr[2].strip())
	
	for i in genre:
		if i in genres:
			genres[i] += 1
		else:
			genres[i] = 1

	
	with open(sys.argv[2], "wt") as f:
		for gen,count in genres.items():
			f.write(str(gen)+" "+ str(count)+"\n")
			

except FileNotFoundError:
	print("데이터 파일이 없습니다")



		
		
