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
		
		#print(act_veh)
		#print(date)
	t1 = zip(base_n,date)
	t2 = zip(act_veh,trips)
	
	dictionary = dict(zip(t1,t2))
	#print(dictionary)


	with open(sys.argv[2], "wt") as f:
		#pass
		for a, b in dictionary.items():
			#for i in a, b:
				#print(a[i],b[i],end="")
			#print('{0}'.format(a))
			c = list(map(int,b))
			f.write(str(a)[1:-1]+str(c)[1:-1]+'\n')
			
		
		
			
		
except FileNotFoundError:
	print("데이터 파일이 없습니다")
