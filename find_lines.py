

#Simple, just gets first sentences that work
def get_lines(t,sentences,important):
	five = t[0]
	sev = t[1]

	first_line = []
	sec_line = []
	third_line = []
	for i in range(0,len(five)):
		if len(five[i]) > 0:
			tup = five[i][0]
			sent = sentences[i]
			for j in range(tup[0],tup[1]+1):
				first_line.append(sent[j])
			if check_important(first_line,important):
				five.pop(i)
				sev.pop(i)
				sentences.pop(i)
				break
			else:
				first_line = []
	for i in range(0,len(five)):
		if len(five[i]) > 0:
			tup = sev[i][0]
			sent = sentences[i]
			for j in range(tup[0],tup[1]+1):
				sec_line.append(sent[j])
			if check_important(sec_line,important):
				five.pop(i)
				sev.pop(i)
				sentences.pop(i)
				break
			else:
				sec_line = []
	for i in range(0,len(five)):
		if len(five[i]) > 0:
			tup = five[i][0]
			sent = sentences[i]
			for j in range(tup[0],tup[1]+1):
				third_line.append(sent[j])
			if check_important(third_line,important):
				five.pop(i)
				sev.pop(i)
				sentences.pop(i)
				break
			else:
				third_line = []
	return [first_line,sec_line,third_line]

def check_important(l,important):
	for w in l:
		if w in important:
			return True
	return False




#Idea for a better evaluation of which sentences are better pending





