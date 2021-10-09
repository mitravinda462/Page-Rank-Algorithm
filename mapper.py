#!/usr/bin/env python3
"""mapper.py"""
import sys
for line in sys.stdin:
	try:
		line = line.strip()
		if(line=='' or line[0]=='#'):
			continue
		print(line)
	except:
		continue
