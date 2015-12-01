##
## This program counts the number of syllables in an input string
##
##
##

import re
import string

def count_syllables(input_string):
	# declare variable to hold count
	syb_count = 0

	# Change to upper case, split input string into words
	words = input_string.upper().split();

	# Loop thru words and count
	for i in words:
		with open('./modified-cmu-new.txt', 'r') as myFile:
			for num, line in enumerate(myFile, 1):
				if i in line:
					# If true: word by itself
					if re.findall("\\b"+i+"\\b", line):
						print line
						# Calculate number of syllables in word
						num_in_word = num_syllables(line)

						# Add to line count
						syb_count = syb_count + num_in_word

					# Else, word within words--we don't want this
					else: 
						continue
						
	# Final count
	print "total count", syb_count

def num_syllables(line):
	s = line.split()
	count = 1
	num_dashes = s.count("-")
	count = count+num_dashes
	return count

def main():
	stop = False

	while (stop == False):
		# Get input token from user
		count_me = raw_input("Enter string to count: ")

		# Strip punctuation
		for c in string.punctuation:
			count_me=count_me.replace(c, "")

		count_syllables(count_me)

		# Continue or break out of loop
		cont = raw_input("\nEnter X to exit, or enter to continue: ")
		if (cont == 'X' or cont == "x"):
			stop = True
		else: 
			continue
	print("Done!")

main()
