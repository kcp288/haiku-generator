

#Simple, just gets first sentences that work
def get_lines(t,sentences,important):
	five = t[0]
	sev = t[1]

	first_line = []
	sec_line = []
	third_line = []
	i =0
	while i < len(five) :
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
		if len(first_line) > 0:
			break
		i +=1

	i =0
	while i < len(sev) :
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
		if len(sec_line) > 0:
			break
		i +=1

	i=0
	while i < len(five) :
		for k in range(0,len(five[i])):
			print('something')
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
		if len(third_line) > 0:
			break
		i +=1
	return [first_line,sec_line,third_line]

def check_important(l,important):
	for w in l:
		if w in important:
			return True
	return False

"""
sentences = [['we','are','your','friends','dont','ever','go','against'],['you','are','my','lightning','in','a','bottle'],['last','sentence','very','short']]
f = [[(0,4),(1,5),(2,6)],[(0,3),(1,4),(3,6)],[(0,2),(1,3)]]
s = [[(0,6),(1,7)],[(0,5),(1,6)],[]]
tup = (f,s)
imp = ['friends','lightning','sentence']

out = get_lines(tup,sentences,imp)
print(out[0])
print(out[1])
print(out[2])
"""


#Idea for a better evaluation of which sentences are better pending





