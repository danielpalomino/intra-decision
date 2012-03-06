import sys

cfgFile = sys.argv[1]
videoPath = sys.argv[2]
frames = sys.argv[3]

video = videoPath.split('/')
videoPath = video[0] + '/videos/' + video[3]

fp = open(cfgFile, 'r')
buff = fp.readlines()
fp.close()
fp = open(cfgFile, 'w')
for line in buff:
	lista = line.split()
	if lista[0] == 'InputFile':
		linha = lista[0] + '\t'+ lista[1] + ' ' + videoPath + '\n'
		fp.write(linha)		
	elif lista[0] == 'FrameToBeEncoded':
		linha = lista[0] + '\t' + lista[1] + ' '  + frames + ' ' + lista[3] + ' ' + lista[4] + ' ' + lista[5] + ' ' + lista[6] + ' ' + lista[7] + ' ' + lista[8] + ' ' + lista[9] + '\n'
		fp.write(linha)
	else:
		fp.write(line)
fp.close()
