"""

Parses all csv files in a specified directory and stores the 
number of times each note has been played in each file in a 
csv file named "final_df.csv"



Example:

	$ python csv-parser.py 

	running the previous line will output to a final_df.csv file
	a dataframe where columns denote each note rows denote each 
	file in the "/midi-csv-files/csv/" path and each datapoint is 
	the number of times the note has been played in the .mid file

Dependencies: 
	pandas

TODO: 
	sort the columns after adding all files
	check that analysis is correct for 5 randomly chosen files
	check that no duplicate columns exist in final_df

"""

import sys, os, pandas as pd

__author__ = "Azzam Althagafi"
__copyright__ = "Copyright 2017, Azzam Althagafi"
__license__ = "MIT"
__email__ = "aazzam@seas.upenn.edu"


rel_path = '/midi-csv-files/csv/'
abs_path = os.getcwd() + rel_path


final_df = pd.DataFrame()  #empty df

# each file is analyzed and then the frequency analysis is appended to the final_df
for filename in os.listdir(abs_path):
	my_cols = [1, 2, "event", 4, "note", 6, 7]

	# When importing csv, we name columns to avoid tokenizing data error
	# This occurs because Time_signature events have 7 columns, while notes have
	# 6 columns.
	df = pd.read_csv(abs_path + filename, names=my_cols)

	# According to midicsv, a note is either "Note_on_c" or "Note_off_c"
	# notes contains an array of all the notes played in chronological order.
	note_events = df[(df.event == " Note_on_c") | (df.event == " Note_off_c")]
	notes = note_events.note
	note_frequencies = notes.value_counts().rename(filename)
	final_df = final_df.append(note_frequencies)

# the final dataframe which contains the note frequency analysis of all files are
# written to a csv file.
final_df.to_csv("final_df.csv")
