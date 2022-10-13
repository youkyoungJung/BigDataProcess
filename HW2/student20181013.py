#!/usr/bin/python3

import openpyxl

wb = openpyxl.load_workbook("student.xlsx")
ws = wb['Sheet1']

#total
row_id = 1

for row in ws:
	if row_id != 1:
		sum_v = ws.cell(row=row_id, column=3).value * 0.3
		sum_v += ws.cell(row=row_id, column=4).value * 0.35
		sum_v += ws.cell(row=row_id, column=5).value * 0.34
		sum_v += ws.cell(row=row_id, column=6).value 
		ws.cell(row=row_id, column=7).value = sum_v
	row_id += 1
	
#grade

#scores=> put total
row_id = 1
scores = []

for row in ws:
	if row_id != 1:
		scores.append(ws.cell(row=row_id, column=7).value)
	row_id += 1

#rankings
rankings = [None]*len(scores)
for i in range(len(scores)):
	rankings[i] = len(scores)
	
	for j in range(len(scores)):
		if scores[j] < scores[i]:
			rankings[i] -= 1			

			
#for i in range(len(rankings)):
print(rankings)

#row_id = 2;
#for i in range(len(scores)):
#	ws.cell(row=row_id, column=9).value = rankings[i]
#	row_id += 1
	
#grade부여

row_id = 2
count = 0

for i in range(len(scores)):
	print(i, len(scores))

	if len(scores)*0.3*0.5/len(scores) >= rankings[i]/len(scores):
		ws.cell(row=row_id, column=8).value = 'A+'
		count += 1
		print("count: ",count)
		row_id += 1
	elif len(scores)*0.3/len(scores) >= rankings[i]/len(scores):
		ws.cell(row=row_id, column=8).value = 'A0'
		count += 1
		print("count: ",count)
		row_id += 1
	elif len(scores)*0.7*0.5/len(scores) >= rankings[i]/len(scores):
		ws.cell(row=row_id, column=8).value = 'B+'
		count += 1
		print("count: ",count)
		row_id += 1
	elif len(scores)*0.7/len(scores) >= rankings[i]/len(scores):
		ws.cell(row=row_id, column=8).value = 'B0'
		count += 1
		print("count: ",count)
		row_id += 1
	elif ((len(scores) - (len(scores)*0.7))*0.5) <= len(scores)-rankings[i]:
		if(len(scores)-rankings[i]) != 0:
			print("c+")
			ws.cell(row=row_id, column=8).value = 'C+'
			row_id += 1
	
	else:
		ws.cell(row=row_id, column=8).value = 'C0'
		print("count: ",count)
		row_id += 1


wb.save("student.xlsx")
