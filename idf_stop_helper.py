import sys

#Code for converting stop words and idf data into list and dictionary repsectively

def get_stop():
	raw_string = open("stop_words.txt").read()	
	stop_words = raw_string.split()
	return stop_words

def get_idf():
	#raw_string = open("idf_training.txt",'r')
	raw_string = open("idf_training.txt").read()
	# print(raw_string)
	idf_dict = {}
	for line in raw_string:
		sline = line.split()
		if len(sline) != 2:
			#print("Something wrong, idf_trained file line != 2")
			continue
		idf_dict[str(sline[0])] = float(sline[1])
	return idf_dict

#print(get_idf())
