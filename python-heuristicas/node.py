class Node:

	def __init__(self):
		self.size = 0
		self.mode = 0
		self.modesForFullRD = []
		self.sun0 = None
		self.sun1 = None
		self.sun2 = None
		self.sun3 = None

	def addModeForFullRD(self,mode):
		if not (mode in self.modesForFullRD):
			self.modesForFullRD.append(mode)
