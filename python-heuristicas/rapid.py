fp = open('allVideosCount.csv','r')
buff = fp.readlines()
fp.close()
fp = open('allVideosCountRight.csv','w')
for line in buff:
	lista = line.split(';')
	new_line = ''
	for elem in lista:
		new_line = new_line + elem + ','
	new_line = new_line[:-1]
	fp.write(new_line)
fp.close()
	
