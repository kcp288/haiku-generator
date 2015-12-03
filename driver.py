import important_words
import sent_parser
import syllabify


def main():
	# This is where we get the text input
	text_input = "This is my example text."

	# Calculate important words - returns array of important words
	important = important_words.wordlist_string(text_input)

	# Get sentences with words
	# Count words in each important sentence
	important_sentences, counts = sent_parser(important, text_input)

	

main()