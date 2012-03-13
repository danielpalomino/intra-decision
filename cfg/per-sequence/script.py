import os
import sys

cfgs = [
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
'NebutaFestival_10bit.cfg',
'ParkScene.cfg',
'PartyScene.cfg',
'PeopleOnStreet.cfg',
'RaceHorsesC.cfg',
'RaceHorses.cfg',
'SlideEditing.cfg',
'SlideShow.cfg',
'SteamLocomotiveTrain_10bit.cfg',
'Traffic.cfg',
'Vidyo1.cfg',
'Vidyo3.cfg',
'Vidyo4.cfg'
]

videos = [
'BasketballDrill_832x480_50.yuv',
'BasketballDrillText_832x480_50.yuv',
'BasketballDrive_1920x1080_50.yuv',
'BasketballPass_416x240_50.yuv',
'BlowingBubbles_416x240_50.yuv',
'BQMall_832x480_60.yuv',
'BQSquare_416x240_60.yuv',
'BQTerrace_1920x1080_60.yuv',
'Cactus_1920x1080_50.yuv',
'ChinaSpeed_1024x768_30.yuv',
'Kimono1_1920x1080_24.yuv',
'NebutaFestival_2560x1600_60_10bit_crop.yuv',
'ParkScene_1920x1080_24.yuv',
'PartyScene_832x480_50.yuv',
'PeopleOnStreet_2560x1600_30_crop.yuv',
'RaceHorses_416x240_30.yuv',
'RaceHorses_832x480_30.yuv',
'SlideEditing_1280x720_30.yuv',
'SlideShow_1280x720_20.yuv',
'SteamLocomotiveTrain_2560x1600_60_10bit_crop.yuv',
'Traffic_2560x1600_30_crop.yuv',
'vidyo1_720p_60.yuv',
'vidyo3_720p_60.yuv',
'vidyo4_720p_60.yuv'
]

frames = sys.argv[1]

for i in range(0,len(videos)):
	path = 'python cfgs.py ' + cfgs[i] + ' ../../videos/' + videos[i] + ' ' + frames
	print path
	os.system(path)
