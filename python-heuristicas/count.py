from __future__ import division
import sys
from node import Node

def createTreeBlock(node,size,mode,fp,level):
	if (int(size) == level):
		node.size = int(size)
		node.mode = int(mode)
		return
	else:
	 	node.size = int(size)
		node.mode = int(mode)
		node.sun0 = Node()
		createTreeBlock(node.sun0,fp.readline(),fp.readline(),fp,level)
		node.sun1 = Node()
		createTreeBlock(node.sun1,fp.readline(),fp.readline(),fp,level)
		node.sun2 = Node()
		createTreeBlock(node.sun2,fp.readline(),fp.readline(),fp,level)
		node.sun3 = Node()
		createTreeBlock(node.sun3,fp.readline(),fp.readline(),fp,level)

count_all = 0
count_equal = 0

def heuristic0(root):
	global count_all,count_equal
	if (root.size == 4):
		return root.mode
	else:
		count_all = count_all + 1
		mode0 = heuristic0(root.sun0)
		heuristic0(root.sun1)
		heuristic0(root.sun2)
		heuristic0(root.sun3)
		if mode0 == root.mode:
			count_equal = count_equal + 1
		return root.mode

def heuristic1(root):
	global count_all,count_equal
	lista = []
	if (root.size == 4):
		return root.mode
	else:
		count_all = count_all + 1
		lista.append(heuristic1(root.sun0))
		lista.append(heuristic1(root.sun1))
		lista.append(heuristic1(root.sun2))
		lista.append(heuristic1(root.sun3))
		if lista.count(root.mode) > 0:
			count_equal = count_equal + 1
		return root.mode

modos_cont = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def moda(m0,m1,m2,m3):
	moda_list = []
	#zerar vetor
	for i in range(0,len(modos_cont)):
		modos_cont[i] = 0
	
	modos_cont[m0] = modos_cont[m0] + 1
	modos_cont[m1] = modos_cont[m1] + 1
	modos_cont[m2] = modos_cont[m2] + 1
	modos_cont[m3] = modos_cont[m3] + 1
	maior = -1
	#achar o maior
	for cont in modos_cont:
		if cont > maior:
			maior = cont
			
	for i in range(0,len(modos_cont)):
		if modos_cont[i] == maior:
			moda_list.append(i)
	return moda_list	

def heuristic2(root):
	global count_all, count_equal
	if (root.size == 4):
		return root.mode
	else:
		count_all = count_all + 1
		mode0 = heuristic2(root.sun0)
		mode1 = heuristic2(root.sun1)
		mode2 = heuristic2(root.sun2)
		mode3 = heuristic2(root.sun3)
		moda_list = moda(mode0,mode1,mode2,mode3)
		if moda_list.count(root.mode) > 0:
			count_equal = count_equal + 1
		return root.mode


modeFile = sys.argv[1]
heuristic = int(sys.argv[2])

fp = open(modeFile, 'r')

fp.seek(0,2)
size = fp.tell()
fp.seek(0,0)

while fp.tell() < size:
	rootNode = Node()
	rootSize = fp.readline()
	rootMode = fp.readline()
	createTreeBlock(rootNode,rootSize,rootMode,fp,4)
	if heuristic == 0:
		heuristic0(rootNode)
	elif heuristic == 1:
		heuristic1(rootNode)
	else:
		heuristic2(rootNode)
total = count_equal/count_all
print str(total*100.00)
