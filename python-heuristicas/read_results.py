from result import Result
import sys

results_list = [
[#'Traffic0.results',
#'PeopleOnStreet0.results',
#'Kimono0.results',
#'ParkScene0.results',
#'Cactus0.results',
#'BasketballDrive0.results',
#'BQTerrace0.results',
#'BasketballDrill0.results',
#'BQMall0.results',
#'PartyScene0.results',
#'RaceHorses0.results',
#'BasketballPass0.results',
#'BQSquare0.results',
#'BlowingBubbles0.results',
#'RaceHorsesC0.results',
#'Vidyo10.results',
#'Vidyo30.results',
#'Vidyo40.results',
#'BasketballDrillText0.results',
#'ChinaSpeed0.results',
#'SlideEditing0.results',
#'SlideShow0.results'
],
[
'Traffic1.results',
'PeopleOnStreet1.results',
'Kimono1.results',
'ParkScene1.results',
'Cactus1.results',
'BasketballDrive1.results',
'BQTerrace1.results',
'BasketballDrill1.results',
'BQMall1.results',
'PartyScene1.results',
'RaceHorses1.results',
'BasketballPass1.results',
'BQSquare1.results',
'BlowingBubbles1.results',
'RaceHorsesC1.results',
'Vidyo11.results',
'Vidyo31.results',
'Vidyo41.results',
'BasketballDrillText1.results',
'ChinaSpeed1.results',
'SlideEditing1.results',
'SlideShow1.results'
],
[
#'Traffic2.results',
#'PeopleOnStreet2.results',
#'Kimono2.results',
#'ParkScene2.results',
#'Cactus2.results',
#'BasketballDrive2.results',
#'BQTerrace2.results',
#'BasketballDrill2.results',
#'BQMall2.results',
#'PartyScene2.results',
#'RaceHorses2.results',
#'BasketballPass2.results',
#'BQSquare2.results',
#'BlowingBubbles2.results',
#'RaceHorsesC2.results',
#'Vidyo12.results',
#'Vidyo32.results',
#'Vidyo42.results',
#'BasketballDrillText2.results',
#'ChinaSpeed2.results',
#'SlideEditing2.results',
#'SlideShow2.results'
]
]

reference = [
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]]
]
results_h0_depth8 = [
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]]
]
results_h0_depth16 = [
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]]
]
results_h0_depth32 = [
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]]
]
results_h0_depth64 = [
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]],
[[[],[],[],[]],[[],[],[],[]]]
]


def read_profile(fp_result,video,profile):
	#READ QP
	qp = int(fp_result.readline())
#	print str(qp)
	#READ DEPTH
	depth = int(fp_result.readline())
#	print str(depth)
	result = Result()
	#READ BITS
	result.bits = float(fp_result.readline())
#	print str(result.bits)
	#READ Y_PSNR
	result.Y_PSNR = float(fp_result.readline())
#	print str(result.Y_PSNR)
	#READ U_PSNR
	result.U_PSNR = float(fp_result.readline())
#	print str(result.U_PSNR)
	#READ V_PSNR
	result.V_PSNR = float(fp_result.readline())
#	print str(result.V_PSNR)
	#READ TIME
	result.time = float(fp_result.readline())
#	print str(result.time)
	if qp == 22:
		j=0
	elif qp == 27:
		j=1
	elif qp == 32:
		j=2
	else:
		j=3
	
	if depth == -1:
		reference[video][profile][j].append(result)
	elif depth == 8:
		results_h0_depth8[video][profile][j].append(result)
	elif depth == 16:
		results_h0_depth16[video][profile][j].append(result)
	elif depth == 32:
		results_h0_depth32[video][profile][j].append(result)
	else:
		results_h0_depth64[video][profile][j].append(result)	

target_depth = int(sys.argv[1])

for l in range(0,len(results_list)):
	for k in range(0,len(results_list[l])):
		fp_result = open('Resultados/' + results_list[l][k], 'r')
		#READ HEURISTIC
		heuristic = fp_result.readline()
		#READ VIDEO
		video = fp_result.readline()
		print str(video)
		for i in range(0,8):
			#READ PROFILE
			profile = fp_result.readline()
			for j in range(0,5):
				#HIGH EFFICIENCY
				if profile == 'High Efficiency\n':
					read_profile(fp_result,k,0)
				#LOW COMPLEXITY
				else:
					read_profile(fp_result,k,1)
		fp_result.close()


if target_depth == -1:
	target = reference
	fp_target_HE = open('REF_HE.csv','w')
	fp_target_LC = open('REF_LC.csv','w')
elif target_depth == 8:
	target = results_h0_depth8
	fp_target_HE = open('AI_HE_8.csv','w')
	fp_target_LC = open('AI_LC_8.csv','w')
elif target_depth == 16:
	target = results_h0_depth16
	fp_target_HE = open('AI_HE_16.csv','w')
	fp_target_LC = open('AI_LC_16.csv','w')
elif target_depth == 32:
	target = results_h0_depth32
	fp_target_HE = open('AI_HE_32.csv','w')
	fp_target_LC = open('AI_LC_32.csv','w')
else:
	target = results_h0_depth64	
	fp_target_HE = open('AI_HE_64.csv','w')
	fp_target_LC = open('AI_LC_64.csv','w')

#VIDEOS
for i in range(0,len(target)):
	#PROFILE HE=0, LC=1
	for j in range(0,len(target[i])):
		#QP 22,26,32,37
		for k in range (0,len(target[i][j])):
			#Elementos da lista = Results
			for l in range(0,len(target[i][j][k])):
				bits = str(target[i][j][k][l].bits)
				y_psnr = str(target[i][j][k][l].Y_PSNR)
				u_psnr = str(target[i][j][k][l].U_PSNR)
				v_psnr = str(target[i][j][k][l].V_PSNR)
				time = str(target[i][j][k][l].time)
				#High Efficiency
				if(j == 0):
					fp_target_HE.write(bits + ',' + y_psnr + ',' + u_psnr + ',' + v_psnr + ',' + time + '\n')
				#Low Complexity
				else:
					fp_target_LC.write(bits + ',' + y_psnr + ',' + u_psnr + ',' + v_psnr + ',' + time + '\n')
fp_target_HE.close()
fp_target_LC.close()

