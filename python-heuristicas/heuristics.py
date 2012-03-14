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

def printTreeBlock(root,level):
	if (root.size == 4):
		return
	else:
		if (root.size <= level):
			#print 'size' + str(root.size)
			print str(len(root.modesForFullRD))
			for i in range(0,len(root.modesForFullRD)):
				print str(root.modesForFullRD[i])
		printTreeBlock(root.sun0,level)
		printTreeBlock(root.sun1,level)
		printTreeBlock(root.sun2,level)
		printTreeBlock(root.sun3,level)

#only first		
def heuristic0(root,level):
	if (root.size == 4):
		return root.mode
	else:
		mode0 = heuristic0(root.sun0,level)
		mode1 = heuristic0(root.sun1,level)
		mode2 = heuristic0(root.sun2,level)
		mode3 = heuristic0(root.sun3,level)
		root.addModeForFullRD(mode0)
		if (root.size <= level):
			return root.mode
		else:
			return

#all four
def heuristic1(root,level):
	if (root.size == 4):
		return root.mode
	else:
		mode0 = heuristic1(root.sun0,level)
		mode1 = heuristic1(root.sun1,level)
		mode2 = heuristic1(root.sun2,level)
		mode3 = heuristic1(root.sun3,level)
		root.addModeForFullRD(mode0)
		root.addModeForFullRD(mode1)
		root.addModeForFullRD(mode2)
		root.addModeForFullRD(mode3)
		if (root.size <= level):
			return root.mode
		else:
			return

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

#moda
def heuristic2(root,level):
	if (root.size == 4):
		return root.mode
	else:
		mode0 = heuristic2(root.sun0,level)
		mode1 = heuristic2(root.sun1,level)
		mode2 = heuristic2(root.sun2,level)
		mode3 = heuristic2(root.sun3,level)
		moda_list = moda(mode0,mode1,mode2,mode3)
		for indice in moda_list:
			root.addModeForFullRD(indice)
		if (root.size <= level):
			return root.mode
		else:
			return root.mode

modeFile = sys.argv[1]
level = int(sys.argv[2])
heuristic = int(sys.argv[3])

fp = open(modeFile, 'r')

fp.seek(0,2)
size = fp.tell()
fp.seek(0,0)

if int(level) == 4:
	print str(8)
	print str(0)
	print str(0)
	print str(0)
elif int(level) == 8:
	print str(8)
	print str(16)
	print str(0)
	print str(0)
elif int(level) == 16:
	print str(8)
	print str(16)
	print str(32)
	print str(0)
else:
	print str(8)
	print str(16)
	print str(32)
	print str(64)

while fp.tell() < size:
	rootNode = Node()
	rootSize = fp.readline()
	rootMode = fp.readline()
	createTreeBlock(rootNode,rootSize,rootMode,fp,4)
	if int(heuristic) == 0:
		heuristic0(rootNode,level)
	elif int(heuristic) == 1:
		heuristic1(rootNode,level)
	else:
		heuristic2(rootNode,level)
	
	if int(level) == 4:
		printTreeBlock(rootNode,8)
	elif int(level) == 8:
		printTreeBlock(rootNode,16)
	elif int(level) == 16:
		printTreeBlock(rootNode,32)
	else:
		printTreeBlock(rootNode,64)

