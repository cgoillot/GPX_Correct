GPX_Correct.py corrects .gpx files imported from Strava/Runtastic so that "Moving Time" is closer to "Elapsed Time" when importing them back to Strava.

Note: you cannot use one script to correct both type of the files at the moment.

# Requirements
Python 2.7 (not tested with other versions at the moment) is required.
Don't forget to add C:\Python27\ in your PATH environment variable.

# How to use it?
1. Download and install Python on your computer: https://www.python.org/download/releases/2.7/
Note: A bugfix release, 2.7.13, is currently available. Its use is recommended.
2. Download the .gpx files from Runtastic/Strava
3. Download "GPX_Correct.py"
4. Gather your .gpx files from Runtastic/Strava with the corresponding GPX_Correct.py in the same folder
5. Double click the GPX_Correct.py or run it from the Command Prompt
6. "Output_ExistingFileName.gpx" files are created
7. Import the "Output_ExistingFileName.gpx" files in Strava: https://www.strava.com/upload/select

# Optional argument 
(try if not satisfied with default value)

.gpx files are composed of track points (trkpt) recorded by your device (phone, watch,...)

For each trkpt the below information is recorded:
- latitude (lat)
- longitude (lon)
- time
- altitude (ele)

The high difference between the "Moving Time" and the "Elapsed Time" is due to bad GPS signal.

1. GPX_Correct deletes the records (trkpt) that are too close to each other. 
2. GPX_Correct inserts records to have at least one record every two seconds.

The "gap" value defines how close are two trkpt. If the distance between two trkpt is inferior to the gap value, one of the two trkpt is deleted. You can specify the gap argument. The smaller the gap is, the more records will be deleted. 
By default, gap = 0,0.
From what I have experienced, the gap value must be superior to 0,00001 and inferior to 0,0002.

You can specify the gap value as the 1st argument when running the script.
For example, run this command in the command prompt: GPX_Correct.py 0.0002

# Support
Please feel free to send an email to this address for feedback/support: gpx.correct@gmail.com
