
def estimate(s):
    if s.isupper():
        return len(s)
	word = s.lower()
	vowels = ['a','e','i','o','u']
	est = 0
	if word[-1] == 'e':
		word = word.rstrip('e')
	elif word[-1] == 'y':
		est +=1
	i = 0
	while i < len(word) and word[i] in vowels:
		if word[i] in vowels:
			while (i < len(word)) & (word[i] in vowels):
				i +=1
			est +=1
        if i < len(word):
            break
		i +=1
	return est
