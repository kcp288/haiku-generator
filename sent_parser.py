import important_words,re,syllabify

def parse_sent(s):

	IW = important_words.wordlist_string(s)

	list_doc = re.split('\.|,',s)
	sentences = []
	sent_syllables = []
	for sent in list_doc:
		l = sent.split()
		for word in IW:
			if word in l:
				syllables = syllabify.count_syllables(l)
				sentences.append(l)
				sent_syllables.append(syllables)
				break

	if len(sentences) <3:
		print('Error not enough sentences')
		return None
	return (sentences,sent_syllables)

	


