import important_words
import sent_parser
import syllabify
import haiku_algorithm
import find_lines
import sys 
import re

def drive():
#def main(f):

	# Calculate important words - returns array of important words
	#important = important_words.wordlist_string(text_input, 10)

	# Get sentences with words
	# INPUT VERSION
	f = sys.stdin.readline()
	if len(f) < 5:
		print ('')
		return None

	important_sentences, counts = sent_parser.parse_sent(f)

	offsets = haiku_algorithm.find_haiku(counts)
	
	lines = find_lines.get_lines(offsets, important_sentences)

	output = ''
	for i in lines:
		line = ' '.join([str(x) for x in i])
		output += line + ' * '

	print (output)
	
	return output


drive()