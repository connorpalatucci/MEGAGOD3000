import nltk
from nltk import word_tokenize
from nltk.corpus import brown
import string
import re
import os


def cleanCorpus( rawCorpusFilename ):
	
	file = open(rawCorpusFilename, 'rt', errors='ignore')
	raw = file.read()
	file.close()


	# print("---------RAW SAMPLE------------")
	# print(raw[:500])


	#remove short lines
	lines = raw.splitlines()
	shortRemoved = [s for s in lines if len(s) >10]
	raw='\n'.join(shortRemoved)

	# print("---------NO SHORT LINES------------")
	# print(raw[:500])


	#remove non-ascii
	raw = raw.encode('ascii', errors='ignore').decode()

	# print("---------ASCII ONLY------------")
	# print(raw[:500])


	#lowercase
	raw = raw.lower()

	# print("---------LOWER------------")
	# print(raw[:500])


	#remove punctuation other than periods
	a = string.punctuation.replace('.', '')
	table = str.maketrans('', '', a)
	raw = raw.translate(table)

	# print("---------NO PUNC------------")
	# print(raw[:500])


	#remove numbers
	table2 = str.maketrans('', '', string.digits)
	raw = raw.translate(table2)

	# print("---------NO NUM------------")
	# print(raw[:500])


	#remove non-words
	wordsDictionary = set(nltk.corpus.brown.words())

	raw = " ".join(w for w in nltk.word_tokenize(raw) \
	         if w.lower() in wordsDictionary or not w.isalpha())

	# print("---------NON WORRDS REMOVED------------")
	# print(raw[:500])


	#replace periods with newlines then remove all other periods
	raw = raw.replace(' . ', '\n')
	raw = raw.replace('.', '')

	# print("---------SENTENCE FORMAT------------")
	# print(raw[:500])

	#create new corpus file
	newFileName, ext = os.path.splitext(rawCorpusFilename)
	newFileName = newFileName + "_CLEANED"
	new = open(newFileName+ext, "w+")
	new.write(raw)
	new.close()
	
	return newFileName+ext;


# #string of entire text document
# raw = file.read()
# file.close()

# print("---------RAW SAMPLE------------")
# print(raw[:500])

# #remove short lines
# lines = raw.splitlines()
# shortRemoved = [s for s in lines if len(s) >10]
# raw='\n'.join(shortRemoved)

# print("---------NO SHORT LINES------------")
# print(raw[:500])

# #remove non-ascii
# raw = raw.encode('ascii', errors='ignore').decode()

# print("---------ASCII ONLY------------")
# print(raw[:500])

# #lowercase
# raw = raw.lower()

# print("---------LOWER------------")
# print(raw[:500])

# #remove punctuation other than periods
# a = string.punctuation.replace('.', '')
# table = str.maketrans('', '', a)
# raw = raw.translate(table)

# print("---------NO PUNC------------")
# print(raw[:500])

# #remove numbers
# table2 = str.maketrans('', '', string.digits)
# raw = raw.translate(table2)

# print("---------NO NUM------------")
# print(raw[:500])


# #remove non-words

# wordsDictionary = set(nltk.corpus.brown.words())

# raw = " ".join(w for w in nltk.word_tokenize(raw) \
#          if w.lower() in wordsDictionary or not w.isalpha())

# print("---------NON WORRDS REMOVED------------")
# print(raw[:500])

# #replace periods with newlines then remove all other periods
# raw = raw.replace(' . ', '\n')
# raw = raw.replace('.', '')

# print("---------SENTENCE FORMAT------------")
# print(raw[:500])




# # #tokenize words
# # tokens = word_tokenize(raw)


# # out = ' '.join(words)

# # print(out[:500])

# out_file = open("corpuscleaned6.txt", "w+")
# out_file.write(raw)
# out_file.close()







# words = text.split()
# print(words[:100])

# import string
# table = str.maketrans('', '', string.punctuation+';')
# stripped = [w.translate(table) for w in words]
# print(stripped[:100])

# words = [word.lower() for word in stripped]
# print(words[:100])