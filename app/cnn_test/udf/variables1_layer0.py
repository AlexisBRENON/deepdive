#! /usr/bin/env python
#Author: Amir S 

from helper.easierlife import *
import json
import fileinput
import numpy

BlockSize=3
FeatureID=1
MAX_IMG_SIZE=32
for row in fileinput.input():
	obj = json.loads(row)
	image_id = obj["image_id"]
	xs= obj["xs"]
	ys= obj["ys"]
	values = obj["values"]
	fid = obj["fid"]
	max_x=max(xs)+1
	max_y=max(ys)+1

	variables= numpy.zeros(MAX_IMG_SIZE*MAX_IMG_SIZE).reshape((MAX_IMG_SIZE, MAX_IMG_SIZE))
	for i in range(0,len(xs)):
		x=xs[i]
		y=ys[i]
		variables[x][y] = values[i]


	for i in range(0,max_x):
		for j in range(0,max_y):
			if i+BlockSize<=max_x and j+BlockSize<=max_y:
				for f in range(0,FeatureID):
					block=[]
					values=[]
					for r in range(i,i+BlockSize):
						for s in range(j,j+BlockSize):
							block.append("("+str(image_id)+","+str(r)+","+str(s)+","+str(f)+")")
							values.append(variables[r][s])
					print json.dumps({
						"image_id":image_id,
						"Bx":i,
						"By":j,
						"prev_id":block,
						"fid":f
						})
					