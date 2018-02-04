paragraphSentences = 5
paragraphNum = 5

print("BUILDING MODEL")
import markovify
from gtts import gTTS
import os



# Build the model.
import json
jsonModel = json.load(open('text_model_EXPORT.txt', 'r'))
text_model = markovify.NewlineText.from_json(jsonModel)

def generateGod():
	

	print("RECIEVING REVELATION")
	#generate sacred text

	# Print five randomly-generated sentences

	sacredExport = ''

	for i in range(paragraphNum):
		sacredExport += str(i+1)
		sacredExport += '. \n'

		for j in range(paragraphSentences):
			newSen = text_model.make_sentence()
			sacredExport += str(newSen) + '.\n'
			
		sacredExport += '\n\n'

	tts = gTTS(text=sacredExport, lang='en')
	tts.save('app/static/sacredExport.mp3')

	return sacredExport;