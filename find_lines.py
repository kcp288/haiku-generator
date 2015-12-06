

#Simple, just gets first sentences that work
def get_lines(t,sentences,important):
	five = t[0]
	sev = t[1]

	first_line = []
	sec_line = []
	third_line = []
	i =0
	while i < len(five):
		# Bug because I modify length of five in the loop
		for k in range(0,len(five[i])):
			if len(five[i]) > 0:
				tup = five[i][k]
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
		i +=1
	i =0
	while i < len(sev):
		for k in range(0,len(sev[i])):
			if len(sev[i]) > 0:
				tup = sev[i][k]
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
		i +=1
	i=0
	while i < len(five):
		for k in range(0,len(five[i])):
			if len(five[i]) > 0:
				tup = five[i][k]
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
		i +=1
	return [first_line,sec_line,third_line]

def check_important(l,important):
	for w in l:
		if w in important:
			return True
	return False




#Idea for a better evaluation of which sentences are better pending





