import re

def count_syllables(input_string):
	# Create the dictionary file
	output = open('./output.txt', 'w')

	
	# declare variable to hold cound
	syb_count = 0

	# Read from dictionary

	syb_source = open('./modified-cmu.txt', 'r')
	#print len(syb_source)

	words = input_string.split();
	print words

	for i in words:
		with open('./test-cmu.txt', 'r') as myFile:
			for num, line in enumerate(myFile, 1):
				if i in line:

					# If true: word within other words
					if re.search("^"+i+"$", line):
						print line

						num_in_word = num_syllables(line)
						print num_in_word

						syb_count = syb_count + num_in_word
					# Else, just the word
					else: 
						print "okay"
						

	print "final count", syb_count


def num_syllables(line):
	print "this was called"
	s = line.split()

	count = 1

	num_dashes = s.count("-")
	count = count+num_dashes
	return count

	'''
		for i in words:


		# If no dashes, 
		if a.count("-") == 0:


	for line in words:
		if "AA" in line: 
			# Split items into list items
			s = line.split()

			# See if "AA" is within word
			if s.count("AA") == 0:
				continue	
			else:
				ndx = s.index("AA")
				count_aa += 1

			# Format output to contain only surrounding phones

			# If "AA" is first phone
			if ndx==1:
				# If "AA" is only phone
				if len(s) == 2: 
					trunc = s[0] + ', ' + s[ndx] + '\n'

				# Else, take AA and following phone
				else: 
					trunc = s[0] + ', ' + s[ndx] + ', ' + s[ndx+1] + '\n'
			
			# If "AA" is last phone
			elif ndx==(len(s)-1):
				trunc = s[0] + ', ' + s[ndx-1] + ', ' + s[ndx] + '\n'

			# Somewhere in the middle but way more fresher
			else :
				trunc = s[0] + ', ' + s[ndx-1] + ', ' + s[ndx] + ', ' + s[ndx+1] + '\n'

			printAA = ''.join(trunc)
			output.write(printAA),
			output_aa.write(printAA),

		elif "AE" in line:
			r = line.split()

			if r.count("AE") == 0:
				continue	
			else:
				ndx2 = r.index("AE")
				count_ae += 1 

			# If "AE" is first phone
			if ndx2==1:
				# If "AE" is only phone
				if len(r) == 2: 
					trunc2 = r[0] + ', ' + r[ndx2] + '\n'

				# Else, take AA and following phone
				else: 
					trunc2 = r[0] + ', ' + r[ndx2] + ', ' + r[ndx2+1] + '\n'

			# If "AE" is last phone
			elif ndx2==(len(r)-1) :
				trunc2 = r[0] + ', ' + r[ndx2-1] + ', ' + r[ndx2] + '\n'

			else: 
				trunc2 = r[0] + ', ' + r[ndx2-1] + ', ' + r[ndx2] + ', ' + r[ndx2+1] + '\n'

			printAE = ''.join(trunc2)
			output.write(printAE),
			output_ae.write(printAE),

	print("words with aa: ")
	print(count_aa) 
	print("\nwords with ae: ")
	print(count_ae)
	'''		

	#output.close()
	#words.close()

def main():
	count_syllables("EAT MY SHORTS Y'ALL ACC INTERESTINGLY ACCION AABERG")

main()
