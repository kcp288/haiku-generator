
"""
Algorithm that finds offsets for five and seven syllable word phrases

input: list of syllable of all sentences, where each entry corresponds to list of syllables of a sentence

output: tuple (five_syll,seven_syll)
	where five_syll/seven_syll are lists of tuples for offsets (the count does include jth word)
	i.e. five_syll = [(i1,j1),(i2,j2),...]
"""

def find_haiku(syllables):
	five_syll = []
	seven_syll = []
	for sent in syllables:
		fivers = get_five(sent)
		seveners = get_seven(sent)
		five_syll.append(fivers)
		seven_syll.append(seveners)
	t = (five_syll, seven_syll)
	return t

def total_syllables(fragment,i,j):
	val = 0
	for i in range(i,j+1):
		val += fragment[i]
	return val

def get_five(sentence):
	start = []
	end = []
	for i in range(0,len(sentence)):
		for j in range(i,len(sentence)):
			syll = total_syllables(sentence,i,j)
			if syll == 5:
				start.append(i)
				end.append(j)
	out = []
	for i in range(0,len(start)):
		t = (start[i],end[i])
		out.append(t)
	return out


def get_seven(sentence):
	start = []
	end = []
	for i in range(0,len(sentence)):
		for j in range(i,len(sentence)):
			syll = total_syllables(sentence,i,j)
			if syll == 7:
				start.append(i)
				end.append(j)
	out = []
	for i in range(0,len(start)):
		t = (start[i],end[i])
		out.append(t)
	return out


"""
s = [[2,3,1,1,3,2,1],[2,4,1,4]]
t = find_haiku(s)
print('five offsets')
print(t[0])
print('seven offsets')
print(t[1])
print('\n',s)
"""

