# GPX Correct
This script correct .gpx files imported from Runtastic so that "Moving Time" is closer to "Elapsed Time" when exporting them in Strava.

# Requirements
Python 2.7 (not tested with other versions at the moment) must be set up for running this script. Below is a tutorial to set up Python.
Don't forget to add the C:\Python27\ in your PATH environment variable.

# How to use the script
1. Download and install Python on your computer
2. Download one or more .gpx files from Runtastic
3. Download the script "GPX_Correct.py"
4. Gather your .gpx files with the script "GPX_Correct.py" in the same folder
5. Double click the GPX_Correct.py or run it from the Command Prompt
6. "..._output.gpx" files are created
7. Import the "..._output.gpx" files in Strava: https://www.strava.com/upload/select

# Advanced and Optional feature
.gpx files are composed of track points (trkpt) recorded by your device (phone, watch,...)
For each trkpt the below information is recorded:
- latitude (lat)
- longitude (lon)
- time
- altitude (ele)

The high difference between the "Moving Time" and the "Elapsed Time" is due to bad GPS signal. It is thus required to correct the .gpx file:

1. The script deletes the records (trkpt) that are too close to each other. 
2. The script then inserts records to have at least one record every two seconds.

The "gap" value defines how close are two trkpt. To simplify, if the distance between two trkpt is inferior to the gap value, one of the trkpt is deleted. You can specify the gap argument. The smaller is the gap, the more records are deleted. 
By default, gap = 0,00017. This value was the best working for me.
From what I have experienced, the gap value must be superior to 0,00001 and inferior to 0,0002.

You can specify the gap value as the 1st argument when running the script.
For example, run this command in the command prompt: GPX_Correct.py 0.0002



