import important_words,re,syllabify,sys

def parse_sent(s, IW):

	#list_doc = re.split('\.|,',s)

	s = re.sub('\,', "", s)
	list_doc = s.split('.')

	sentences = []
	sent_syllables = []
	for sent in list_doc:
		l = sent.split()

		for word in l:

			if word.lower() in IW:
				syllables = syllabify.count_syllables(l)
				if syllables == None:
					break
				sentences.append(l)
				sent_syllables.append(syllables)
				break

	if len(sentences) < 3:
		# print('Error not enough sentences')
		return None
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


