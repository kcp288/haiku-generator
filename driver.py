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

	important_word = important_words.wordlist_string(f,10)
	
	# Remove NoneType from list
	important_word = [x for x in important_word if x is not None]

	important_sentences, counts = sent_parser.parse_sent(f, important_word)
	if important_sentences == "ERROR":
		print ('')
		return None
		
	offsets = haiku_algorithm.find_haiku(counts)
	
	lines = find_lines.get_lines(offsets, important_sentences, important_word)

	for i in lines:
		if len(i)==0:
			print ('')
			return None

	output = ''
	for i in lines:
		line = ' '.join([str(x) for x in i])
		output += line + ' * '

	print (output)
	
	return output


drive()