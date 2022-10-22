#!/usr/bin/python
import sys
import calendar

base_n = []
date = []
act_veh = []
trips = []

def get_days(yyyy, mm, dd):
	dayofweek = ["MON", "TUE","WED", "THU","FRI","SAT","SUN"]
	return dayofweek[calendar.weekday(yyyy,mm,dd)]

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
		
	with open(sys.argv[2], "wt") as f:
		for region, day, vehicles, trips in zip(base_n, date, act_veh, trips):
			f.write(str(region) + "," + str(day)
			 + " " + str(vehicles) + "," + str(trips) + "\n")
		
		
			
		
except FileNotFoundError:
	print("데이터 파일이 없습니다")
