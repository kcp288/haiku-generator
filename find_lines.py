

#Simple, just gets first sentences that work
def get_lines(t,sentences):
	five = t[0]
	sev = t[1]

	first_line = []
	sec_line = []
	third_line = []
	for i in range(0,len(five)):
		if len(five[i] > 0):
			tup = five[i][0]
			sent = sentences[i]
			for j in range(tup[0],tup[1]+1):
				first_line.append(sent[j])
			five.pop(i)
			sev.pop(i)
			sentence.pop(i)
			break
	for i in range(0,len(five)):
		if len(five[i] > 0):
			tup = sev[i][0]
			sent = sentences[i]
			for j in range(tup[0],tup[1]+1):
				sec_line.append(sent[j])
			five.pop(i)
			sev.pop(i)
			sentence.pop(i)
			break
	for i in range(0,len(five)):
		if len(five[i] > 0):
			tup = five[i][0]
			sent = sentences[i]
			for j in range(tup[0],tup[1]+1):
				third_line.append(sent[j])
			five.pop(i)
			sev.pop(i)
			sentence.pop(i)
			break
	return [first_line,sec_line,third_line]






#Idea for a better evaluation of which sentences are better pending





