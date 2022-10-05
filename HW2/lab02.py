#!/usr/bin/python3

conf_sum = 0.0
conf_count = 0

with open("mbox-short.txt", "rt") as fp:
	for line in fp:
		if line.startswith("X-DSPAM-Confidence: "):
			str_arr = line.split()
			conf_sum += float(str_arr[1])
			conf_count += 1

print(conf_sum/conf_count)
