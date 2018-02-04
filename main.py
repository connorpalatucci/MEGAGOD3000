

rawCorpusFile = 'corpus.txt'

paragraphSentences = 5
paragraphNum = 15

print("CLEANING")
import cleaner
#cleanedCorpusFile = cleaner.cleanCorpus(rawCorpusFile)
cleanedCorpusFile = 'corpus_CLEANED.txt'

print("BUILDING MODEL")
import markovify

# Get raw text as string.
with open(cleanedCorpusFile) as f:
    text = f.read()

# Build the model.
text_model = markovify.NewlineText(text, state_size=3)

#export model?????
model_json = text_model.to_json()
import json
with open('text_model_EXPORT.txt', 'w') as outfile:
    json.dump(model_json, outfile)


print("RECIEVING REVELATION")
#generate sacred text

# Print five randomly-generated sentences

sacredExport = open('sacredText.txt', "w+")

for i in range(paragraphNum):
	sacredExport.write(str(i+1))
	sacredExport.write('. \n')
	print(str(i+1) + '.')

	for j in range(paragraphSentences):
		newSen = text_model.make_sentence()
		sacredExport.write(str(newSen) + '.\n')
		print(newSen)
	sacredExport.write('\n\n')

sacredExport.close()
	









