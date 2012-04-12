import os

cfgs = ['encoder_intra_22.cfg',
'encoder_intra_27.cfg',
'encoder_intra_32.cfg',
'encoder_intra_37.cfg',
'encoder_intra_loco_22.cfg',
'encoder_intra_loco_27.cfg',
'encoder_intra_loco_32.cfg',
'encoder_intra_loco_37.cfg']

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
'ParkScene.cfg',
'PartyScene.cfg',
'PeopleOnStreet.cfg',
'RaceHorsesC.cfg',
'RaceHorses.cfg',
'SlideEditing.cfg',
'SlideShow.cfg',
'Traffic.cfg',
'Vidyo1.cfg',
'Vidyo3.cfg',
'Vidyo4.cfg'
]

cfg_path = '../cfg/myCfgs/'
sequence_path = '../cfg/per-sequence/'
coder = './TAppEncoderStatic'
param = '-c'
space = ' '
allResults = open('allVideosCount.csv', 'w')

for sequence in sequences:
	allResults.write(sequence + '\n')
	for cfg in cfgs:
		path_coder = coder + ' -c ' + cfg_path + cfg + ' -c ' + sequence_path + sequence
		print path_coder
		os.system(path_coder)
		path_count = 'python count.py modes 1 > count'
		print path_count
		os.system(path_count)
		fp_count = open('count', 'r')
		count = fp_count.readline()
		allResults.write(cfg + ';' + count)
		fp_count.close()
allResults.close()

