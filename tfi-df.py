##
## Calculates TF/IDF given term frequency and inverse document frequency
## 

import math

def tf_idf(docs_containing_term, num_docs, num_in_doc):

	# TF(t) = Freq of term t in doc 
	tf = num_in_doc
	
	# IDF(t) = log_e(total number of docs / number of docs containing term t)
	idf = math.log(num_docs / docs_containing_term)

	#TF-IDF is product
	answer = tf*idf

	print answer

def main():
	num_in_doc = eval(raw_input("Number of times term in doc: "))
	docs_containing_term = eval(raw_input("Number of documents containing terms: "))
	num_docs = eval(raw_input("Number of docs in collection: "))
	tf_idf(float(docs_containing_term), num_docs, num_in_doc)

main()