#!/usr/bin/env python3
"""mapper.py"""
import sys
file=sys.argv[1]
d=dict()
no_in=dict()
with open(file,"r") as f:
	while True:
		line=f.readline()
		if not line:
			break
		node,rank=line.strip().split(",")
		d[node]=float(rank)
		no_in[node]=0
for line in sys.stdin:
    try:
        node,list_nodes=line.split()
        list_nodes=list_nodes.split(",")
        contribution=d[node]/len(list_nodes)
        for i in list_nodes:
            if(i in d):
                print(i,contribution)
            if(i in no_in):
                del no_in[i]
    except:
        continue
for i in sorted(no_in.keys()):
    print(i, no_in[i])
