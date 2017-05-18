"""

Parses a csv file and performs frequency analysis on the notes
played then writes the result to a .txt file.


Example:

	$ python csv-parser.py <file.csv>

	running the previous line will output to a .txt file
	a frequency analysis in the format of 
	note1 - # of note1 played
	note2 - # of note2 played
	where each line represents the note number according to MIDI standards

TODO:
	delete all entries where 2nd column is 0
	store 5th column in a series to perform analysis on notes
	store note frequencies in a .txt file (added to existing values)


Dependencies: 
	pandas

"""

import sys, pandas as pd

__author__ = "Azzam Althagafi"
__copyright__ = "Copyright 2017, Azzam Althagafi"
__license__ = "MIT"
__email__ = "aazzam@seas.upenn.edu"

# commandline arguments
filename = sys.argv[1]

# importing data set using pandas
df = pd.read_csv(filename)

