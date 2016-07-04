# GPX Correct
This script correct .gpx files from Runtastic so that "Moving Time" is closer to "Elapsed Time" when importing them in Strava.

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

# Optional feature
You can specify the gap


The script first delete trkpt (track point) when they are too close to each other
trkpt[i] is deleted if:
|lat[i+1]-lat[i]|<gap and |lon[i+1]-lon[i]|<gap

You can specify the gap value as the 1st argument of the script.
For example, to run the script : run the command: 


