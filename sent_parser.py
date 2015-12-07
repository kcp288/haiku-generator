import important_words,re,syllabify,sys

def parse_sent(s, IW):

	s = re.sub('\,', "", s)
	list_doc = s.split('.')

	# Eliminate blank sentences
	list_doc = [x for x in list_doc if len(x) is not 0]

	sentences = []
	sent_syllables = []

	for sent in list_doc:
		if sent == None:
			break
		l = sent.split()

		for word in l:
			if word == None:
				break
			if word.lower() in IW:
				syllables = syllabify.count_syllables(l)
				if syllables == None:
					break
				sentences.append(l)
				sent_syllables.append(syllables)
				break

	if len(sentences) < 3:
		# print('Error not enough sentences')
		return "ERROR", sent_syllables
	return (sentences,sent_syllables)


'''
raw = open('practice.txt').read()

t = parse_sent(raw)
if (t == None):
	print("not enough sentences")
	sys.exit()
sent = t[0]
syll = t[1]

if len(sent) != len(syll):
	print("Diff lengths")
	sys.exit()

for i in range(0,6):
	print(sent[i])
	print(syll[i])
print(len(sent))
'''


