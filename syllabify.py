##
## This program counts the number of syllables in an input string
## If them checks if there are 5. If so, it stops. Else, it continues. 

import re
import string

# Count syllab

def count_syllables(sentence):

	# declare variable to hold count
	syb_count = 0


	# Change to upper case, split input string into words
	sentence = [i.upper() for i in sentence]
	
	#print ("converted:", sentence)

	# words = sentence.upper()

	syllable_count = []
	# Loop thru words and count
	for i in sentence:
		with open('./modified-cmu-new.txt', 'r') as myFile:
			for num, line in enumerate(myFile, 1):
				if i in line:
					# If true: word by itself
					if re.findall("\\b"+i+"\\b", line):
						#print line
						# Calculate number of syllables in word
						num_in_word = num_syllables(line)
						syllable_count.append(num_in_word)
						# Add to line count
						#syb_count = syb_count + num_in_word

					# Else, word within words--we don't want this
					else: 
						continue
				else:
					return None

	return syllable_count

def num_syllables(line):
	s = line.split()
	count = 1
	num_dashes = s.count("-")
	count = count+num_dashes
	return count

'''

def main():
	output = open('./haiku.txt', 'w')
	input_file = open('./sample.txt', 'r')
	

	# TODO: Replace with important words from tf-idf
	sentence = ['This', 'is', 'a', 'sentence', 'test']

	count = count_syllables(sentence)

	print sentence, count

	# Get strings of 3-6 words with each word in it
	
	for i in important:
			with open('./sample.txt', 'r') as myFile:
				for line in myFile:
					if i in line:
						s = line.split()
						# If true: word by itself
						if (s.index(i) >= 0): 
							idx = s.index(i)
							print s
							print idx

							output_line = s[idx] + s[idx+1] + s[idx+2] + s[idx+4]
							print output_line
						else: continue
						

	#count_syllables(line)

	# Write out 5 and 7 syllable phrases
	# output.write()
	
	output.close()
	input_file.close()

main()
'''