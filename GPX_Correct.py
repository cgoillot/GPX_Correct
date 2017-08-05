#!/usr/bin/python2.7
# GPX_Correct.py corrects .gpx files imported from Runtastic so that "Moving Time" is closer to "Elapsed Time" when exporting them to Strava.

 # Requirements
# Python 2.7 (not tested with other versions at the moment) is required.
# Don't forget to add C:\Python27\ in your PATH environment variable.

 # How to use it?
# 1. Download and install Python on your computer
# 2. Download the .gpx files from Runtastic
# 3. Download "GPX_Correct.py"
# 4. Gather your .gpx files with the "GPX_Correct.py" in the same folder
# 5. Double click the GPX_Correct.py or run it from the Command Prompt
# 6. "..._output.gpx" files are created
# 7. Import the "..._output.gpx" files in Strava: https://www.strava.com/upload/select

 # Optional argument 
# (try if not satisfied with default value)

# .gpx files are composed of track points (trkpt) recorded by your device (phone, watch,...)

# For each trkpt the below information is recorded:
# - latitude (lat)
# - longitude (lon)
# - time
# - altitude (ele)

# The high difference between the "Moving Time" and the "Elapsed Time" is due to bad GPS signal.

# 1. GPX_Correct deletes the records (trkpt) that are too close to each other. 
# 2. GPX_Correct inserts records to have at least one record every two seconds.

# The "gap" value defines how close are two trkpt. If the distance between two trkpt is inferior to the gap value, one of the trkpt is deleted. You can specify the gap argument. The smaller the gap is, the more records will be deleted. 
# By default, gap = 0.
# From what I have experienced, the gap value must be superior to 0,00001 and inferior to 0,0002.

# You can specify the gap value as the 1st argument when running the script.
# For example, run this command in the command prompt: GPX_Correct.py 0.0002

def TimeCorrect(f,output,gap):
	tree = ET.parse(f)
	root = tree.getroot()
	iterator1 = tree.iter(tag='{http://www.topografix.com/GPX/1/1}trkpt')
	lat = []
	lon = []
	number = []
	j=0
	y=0
	sup=0

	for elem1 in iterator1:
		lat.append(Decimal(elem1.get('lat')))
		lon.append(Decimal(elem1.get('lon')))
		number.append(j)
		j+=1

	del number[len(number)-1]
	
	print(Decimal(lat[1]))

	for i in range(0, len(lat)-1):
		if (abs(Decimal(lat[i] - lat[i+1]))>Decimal(gap) or abs(Decimal(lon[i] - lon[i+1]))>Decimal(gap)):
			number[i] = int(-1)

	for trk in root:
		for trkseq in trk:
			for trkpt in trkseq.findall('{http://www.topografix.com/GPX/1/1}trkpt'):
				if y < len(number):
					if number[y] >= 0:
						y+=1
						trkseq.remove(trkpt)
						sup+=1
					else:
						y+=1
	print('number of trkpt cleaned:', sup)
	tree.write(output)

def SpeedCorrect(f):
	tree = ET.parse(f)
	root = tree.getroot()
	iterator2 = tree.iter(tag='{http://www.topografix.com/GPX/1/1}time')
	iterator1 = tree.iter(tag='{http://www.topografix.com/GPX/1/1}trkpt')
	t = []
	lat = []
	lon = []
	number = []
	ref1 = datetime.strptime('3', '%S')
	ref0 = datetime.strptime('0', '%S')
	ref = ref1 - ref0
	i=0
	y=0
	insertion = 0
	
	if ("Runtastic" in (root.get('creator'))):
		for elem2 in iterator2:
			t.append(datetime.strptime(elem2.text, '%Y-%m-%dT%H:%M:%SZ'))
	elif ("Strava" in (root.get('creator'))):
		for elem2 in iterator2:
			t.append(datetime.strptime(elem2.text, '%Y-%m-%dT%H:%M:%SZ'))
			
	for elem1 in iterator1:
		lat.append(Decimal(elem1.get('lat')))
		lon.append(Decimal(elem1.get('lon')))
		number.append(int(0))
	
	print("initial number of trkpt: ", len(number))
	
	while i<len(t)-2:
		delta = t[i+1]-t[i]
		if  delta > ref:
			newlat = lat[i]+(lat[i+1]-lat[i])/2
			newlon = lon[i]+(lon[i+1]-lon[i])/2
			t.insert(i+1,t[i]+delta/2)
			lat.insert(i+1,newlat)
			lon.insert(i+1,newlon)
			number.insert(i+1,1)
		else:
			i+=1
	
	print("new trkpt inserted: ", sum(number))
		
	trk = root.find('{http://www.topografix.com/GPX/1/1}trk')
	trkseg = trk.find('{http://www.topografix.com/GPX/1/1}trkseg')
	trkpt = trkseg.find('{http://www.topografix.com/GPX/1/1}trkpt')
	for i in range(0,len(number)-1):
		if number[i]>0:
			trkseg.insert(0,trkpt)
			insertion+=1
	y=0
	
	tree.write(f)
	tree = ET.parse(f)
	root = tree.getroot()
	
	trackpoint = 0
	
	for trkpt in tree.iter(tag='{http://www.topografix.com/GPX/1/1}trkpt'):
		trkpt.set('lat',str(lat[y]))
		trkpt.set('lon',str(lon[y]))
		y+=1
	j=0
	
	for time in tree.iter(tag='{http://www.topografix.com/GPX/1/1}time'):
		newtime=t[j].strftime('%Y-%m-%dT%H:%M:%S.000Z')
		time.text=str(newtime)
		j+=1
	
	tree.write(f)


if __name__ == '__main__':
	from decimal import *
	from datetime import datetime
	import xml.etree.ElementTree as ET
	import sys
	import os
	getcontext().prec = 16
	ET.register_namespace('', "http://www.topografix.com/GPX/1/1")
	listfile=[]
	outputfile=[]

	for file in os.listdir(os.path.dirname(os.path.abspath(__file__))):
		if file.endswith("output.gpx"):
			outputfile.append(file)
		elif file.endswith(".gpx"):
			listfile.append(file)
		elif file.endswith(".py"):
			pass
		else:
			print("This file is not a gpx file: ", file)
	
	ET.register_namespace('', "http://www.topografix.com/GPX/1/1")
	
	if len(listfile)>0:
		if len(sys.argv) > 1:
			if abs(Decimal(sys.argv[1]))<Decimal(0.001):
				for i in range (0,len(listfile)):
					filename=listfile[i].rstrip(listfile[i][-4:])
					newfilename = "Output_" + filename + ".gpx"
					print("Correcting", filename)
					TimeCorrect(listfile[i], newfilename, Decimal(sys.argv[1]))
					SpeedCorrect(newfilename)
					print(filename, "has been corrected --> ", newfilename, "\n")
			else:
				print("argv1 must be a float type < 0.001 ; 0 used instead for gap value")
		else:
			for i in range (0,len(listfile)):
				filename=listfile[i].rstrip(listfile[i][-4:])
				newfilename = "Output_" + filename + ".gpx"
				print("Correcting", filename)
				TimeCorrect(listfile[i], newfilename, 0)
				SpeedCorrect(newfilename)
				print(filename, "has been corrected --> ", newfilename, "\n")
	else:
		print("no .gpx files in this folder; insert .gpx files in this folder to correct them")

	if len(outputfile)>0:
		print("These files have already been corrected (remove _output.gpx): ")
		for i in range(0, len(outputfile)):
			print(outputfile[i])
		