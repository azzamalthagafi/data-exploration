"""

Parses a csv file and performs frequency analysis on the notes
played then writes the result to a .txt file.


Example:

	$ python csv-parser.py <file.csv>

	running the previous line will output to a nfa_<file>.csv file
	matching each note with the number of times it has been played in the
	.mid file

Dependencies: 
	pandas

"""

import sys, os, pandas as pd

__author__ = "Azzam Althagafi"
__copyright__ = "Copyright 2017, Azzam Althagafi"
__license__ = "MIT"
__email__ = "aazzam@seas.upenn.edu"

# commandline arguments
filename = sys.argv[1]

# When importing csv, we name columns to avoid tokenizing data error
# This occurs because Time_signature events have 7 columns, while notes have
# 6 columns.
my_cols = [1, 2, "event", 4, "note", 6, 7]
df = pd.read_csv(filename, names=my_cols)

# According to midicsv, a note is either "Note_on_c" or "Note_off_c"
# notes contains an array of all the notes played in chronological order.
note_events = df[(df.event == " Note_on_c") | (df.event == " Note_off_c")]
notes = note_events.note

# TODO: ultimate goal is to have a huge df that has in each row a song
# 		and first column would be artist and other columns are notes
#		to achieve this, csv-parser will append a row to a .csv file
#		with the frequencies of the notes in columns.



# (PREVIOUS CODE) This code below was commented to test another way of implementation
# this step creates a value count df for each note.
# note_frequencies = notes.value_counts()

# file writing
#note_frequencies.to_csv("nfa_" + os.path.splitext(filename)[0] + ".csv")




