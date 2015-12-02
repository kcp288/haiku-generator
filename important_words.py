import idf_stop_helper 
# Function returns most important words based on idf from input string/list

def wordlist_string(s,N):
	return wordlist_list(s.split(),N)

def wordlist_list(l,N):
	new_list = []
	for w in l:
		if len(w) < 3:
			continue
		if w.isalpha():
			new_list.append(w.lower())
	return wordlist_list_helper(new_list,N)

def wordlist_list_helper(l,N):
	idf_dict = idf_stop_helper.get_idf()
	stop_words = idf_stop_helper.get_stop()

	tfidf = {}
	special = []
	best = 0
	for w in set(l):
		if w in stop_words:
			continue
		if w in idf_dict:
			tfidf[w] = l.count(w) * idf_dict[w]
			if idf_dict[w] > best:
				best = idf_dict[w]
		else :
			if l.count(w) > 1:
				special.append(w)

	for w in special:
		tfidf[w] = l.count(w) * best 

	i = 0
	out_array = [None]*N
	for word in sorted(tfidf, key=tfidf.get, reverse = True):
		print(i)
		print(word)
		out_array[i] = word
		i +=1
		if i >= N:
			break
	
	return out_array




