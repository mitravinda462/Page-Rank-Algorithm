#!/usr/bin/env python3
"""reducer.py"""
import sys
#curr_contribution=float()
#curr_node = None
contributions={}
for line in sys.stdin:
	try:
		line=line.strip()
		node,contribution=line.split()
		if node in contributions:
			contributions[node]+=float(contribution)
		else:
			contributions[node]=float(contribution)
	except:
		continue
for key in sorted(contributions.keys()):
	rank=0.15+(0.85*contributions[key])
	print("%s,%.5f"%(key, rank))
    #try:
     #   contribution = float(contribution)
    #except ValueError:
     #   continue
    #if curr_node == node:
     #   curr_contribution += contribution
    #else:
     #   if curr_node:
      #      curr_contribution=(0.85*curr_contribution)+0.15
       #     print(curr_node+","+"%.5f" %curr_contribution))
        #curr_contribution = contribution
        #curr_node = node
#if curr_node == node:
 #   contribution=float((0.85*curr_contribution)+0.15)
  #  print(curr_node+","+"%.5f" %contribution))
