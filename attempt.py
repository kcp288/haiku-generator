import important_words
import syllabify

def main():
  print_me = important_words.wordlist_string("try this string of words try this string of important cat words however content president politicians are actually kind of important this is shit and it had better work", 5)
  
  print print_me
  sentence = "This is my test sentence"
  s = sentence.split(' ')
  arrayct = syllabify.count_syllables(s)
  print arrayct

main()
