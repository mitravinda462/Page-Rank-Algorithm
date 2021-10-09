#!/usr/bin/env python3
"""reducer.py"""
import sys
curr_node = None
first_node=None
vertices={}
adj_list=[]
file=sys.argv[1]
for line in sys.stdin:
	try:
		line=line.strip()
		first_node, second_node = line.split()
		if first_node not in vertices:		
			vertices[first_node]=1
		if curr_node == first_node:
			adj_list.append(second_node)
		else:
			if curr_node:
				#line="["
				#for j in adj_list:
				#	line=line+j+","
				#line=line[:len(line)-1]
				#line+="]"
				line=','.join(adj_list)
				print(curr_node,line)
			curr_node = first_node
			adj_list=[second_node]
	except:
		continue
if curr_node == first_node:
	#line="["
	#for j in adj_list:
	#	line=line+j+","
	#line=line[:len(line)-1]
	#line+="]"
	line=','.join(adj_list)
	print(curr_node,line)
with open(file,"w") as f:
	for i in sorted(vertices.keys()):
		f.write("%s,%d\n" % (i,1))
f.close()
