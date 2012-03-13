import os

cfgs = ['encoder_intra_22.cfg',
'encoder_intra_27.cfg',
'encoder_intra_32.cfg',
'encoder_intra_37.cfg',
'encoder_intra_loco_22.cfg',
'encoder_intra_loco_27.cfg',
'encoder_intra_loco_32.cfg',
'encoder_intra_loco_37.cfg']

cfgs_fast = ['encoder_intra_fast_22.cfg',
'encoder_intra_fast_27.cfg',
'encoder_intra_fast_32.cfg',
'encoder_intra_fast_37.cfg',
'encoder_intra_loco_fast_22.cfg',
'encoder_intra_loco_fast_27.cfg',
'encoder_intra_loco_fast_32.cfg',
'encoder_intra_loco_fast_37.cfg']

QP_list = [22,27,32,37,22,27,32,37]

sequences = [
'BasketballDrill.cfg',
'BasketballDrillText.cfg',
'BasketballDrive.cfg',
'BasketballPass.cfg',
'BlowingBubbles.cfg',
'BQMall.cfg',
'BQSquare.cfg',
'BQTerrace.cfg',
'Cactus.cfg',
'ChinaSpeed.cfg',
'Kimono.cfg',
#'NebutaFestival_10bit.cfg',
'ParkScene.cfg',
'PartyScene.cfg',
'PeopleOnStreet.cfg',
'RaceHorsesC.cfg',
'RaceHorses.cfg',
#'RollingTomatoes.cfg',
'SlideEditing.cfg',
'SlideShow.cfg',
#'SteamLocomotiveTrain_10bit.cfg',
'Traffic.cfg',
'Vidyo1.cfg',
'Vidyo3.cfg',
'Vidyo4.cfg'
]

results_list = [
'BasketballDrills',
'BasketballDrillText',
'BasketballDrive',
'BasketballPass',
'BlowingBubbles',
'BQMall',
'BQSquare',
'BQTerrace',
'Cactus',
'ChinaSpeed',
'Kimono',
#'NebutaFestival_10bit',
'ParkScene',
'PartyScene',
'PeopleOnStreet',
'RaceHorsesC',
'RaceHorses',
#'RollingTomatoes',
'SlideEditing',
'SlideShow',
#'SteamLocomotiveTrain_10bit',
'Traffic',
'Vidyo1',
'Vidyo3',
'Vidyo4'
]

heuristic_list = [0,1]

def getResults(allResults,qp,sequence,heuristic,level):
	fp = open('results','r')
	allResults.write(str(qp) + '\n')
	allResults.write(str(level) + '\n')
	buff = fp.readlines()
	for line in buff:
		allResults.write(line)
	fp.close()

cfg_path = '../cfg/myCfgs/'
sequence_path = '../cfg/per-sequence/'
coder = './TAppEncoderStatic'
param = '-c'
space = ' '

for heuristic in heuristic_list:
	for j in range(0,len(sequences)):
		allResults = open(results_list[j] + str(heuristic) + '.results','w')
		allResults.write(str(heuristic) + '\n')
		allResults.write(sequences[j] + '\n')
		for i in range(0,len(cfgs)):
			if i/4 == 0:
				allResults.write('High Efficiency' + '\n')
			else:
				allResults.write('Low Complexity' + '\n')
			###RDO FULL
			path_coder = coder + space + param + space + cfg_path + cfgs[i] + space + param + space + sequence_path + sequences[j]
			print path_coder
			os.system(path_coder)
			getResults(allResults,QP_list[i],sequences[j],-1,-1)
			##NIVEL 8
			path_heur = 'python heuristics.py modes 4 ' + str(heuristic) + ' > input_modes'
			print path_heur
			os.system(path_heur)
			path_coder_fast = coder + space + param + space + cfg_path + cfgs_fast[i] + space + param + space + sequence_path + sequences[j]
			print path_coder_fast
			os.system(path_coder_fast)
			getResults(allResults,QP_list[i],sequences[j],0,8)
			##NIVEL 16
			path_heur = 'python heuristics.py modes 8 ' + str(heuristic) + ' > input_modes'
			print path_heur
			os.system(path_heur)
			print path_coder_fast
			os.system(path_coder_fast)
			getResults(allResults,QP_list[i],sequences[j],0,16)
			##NIVEL 32
			path_heur = 'python heuristics.py modes 16 ' + str(heuristic) + ' > input_modes'
			print path_heur
			os.system(path_heur)
			print path_coder_fast
			os.system(path_coder_fast)
			getResults(allResults,QP_list[i],sequences[j],0,32)
			##NIVEL 64
			path_heur = 'python heuristics.py modes 32 ' + str(heuristic) + ' > input_modes'
			print path_heur
			os.system(path_heur)
			print path_coder_fast
			os.system(path_coder_fast)
			getResults(allResults,QP_list[i],sequences[j],0,64)
		allResults.close()
