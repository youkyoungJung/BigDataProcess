#!/usr/bin/python
import sys
import calendar

  
base_n = []
date = []
act_veh = []
trips = []

def get_days(yyyy, mm, dd):
	dayofweek = ["MON", "TUE","WED", "THU","FRI","SAT","SUN"]
	a = dayofweek[calendar.weekday(yyyy,mm,dd)]
	return a

try:
	with open(sys.argv[1], "rt") as f:
		for line in f:
			data = line.split(",")
			base_n.append(data[0].strip())
			mm = int(data[1].split("/")[0])
			dd = int(data[1].split("/")[1])
			yyyy = int(data[1].split("/")[2]) 
			date.append(get_days(yyyy,mm,dd))
			act_veh.append(data[2].strip())
			trips.append(data[3].strip())
		


	t1 = zip(base_n,date)
	t2 = zip(act_veh,trips)
	t3 = zip(t1,t2)
	
	dictionary = dict()
	his_dict = dict()
		
	for a,b in t3:
		if a not in dictionary:
			dictionary[a] = b
			his_dict[a] = b
			#print("생성 dict",a,dictionary[a])
		elif a in dictionary:
			#*a,b = zip(*t3)
			dictionary[a] = dictionary[a] + b
			#print("추가해야할 dict",a,dictionary[a])
			
			#dictionary[a] = b


		
		
		
	with open(sys.argv[2], "wt") as f:
		#pass
		sum_1 = 0
		sum_2 = 0
		for a,b in dictionary.items():
			for i in range(len(a)):
				if i % 2 == 0:
					sum_1 += int(b[i])
				else:
					sum_2 += int(b[i])
			
			print(a, sum_1, sum_2)	
		
		#for a, b in dictionary.items():
			#print(a[0])
			#print(list(map(int, b)))
			f.write("{},{} {},{}\n" .format(a[0],a[1],sum_1,sum_2))
			sum_1 = 0
			sum_2 = 0
			
		
		
			
		
except FileNotFoundError:
	print("데이터 파일이 없습니다")
