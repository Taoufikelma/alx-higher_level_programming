#!/usr/bin/python3
import sys
a = len(sys.argv)
total = 0
for i in range(a - 1):
	total += int(sys.argv[i+1])
print("{}".format(total))
