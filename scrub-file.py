scrub_me = open('./modified-cmu.txt', 'r')
output = open('./modified-cmu-new.txt', 'w')

for line in scrub_me:
	s = line.split()
	if "-" in s[0]:
		print s[0]
	elif "'" in s[0]:
		print s[0]
	elif "(" in s[0]:
		print s[0]
	elif "." in s[0]:
		print s[0]
	else:
		output.write(line)

scrub_me.close() 