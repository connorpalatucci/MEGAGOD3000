from app import app
from flask import render_template, url_for
import megagod
import cleaner
import os
from random import choice


@app.route('/')
@app.route('/index')
def index():

	def random_video():
		names = os.listdir(os.path.join(app.static_folder, 'videos'))
		print(names)
		selected = choice(names)
		print(selected)
		ugh = 'videos/' + selected
		print(ugh)
		videoPathText = url_for('static', filename=ugh)
		#videoPathText = os.path.join(app.static_folder, 'videos', selected)
		return videoPathText

	def random_sound():
		names = os.listdir(os.path.join(app.static_folder, 'sounds'))
		print(names)
		selected = choice(names)
		print(selected)
		ugh = 'sounds/' + selected
		print(ugh)
		soundPathText = url_for('static', filename=ugh)
		#videoPathText = os.path.join(app.static_folder, 'videos', selected)
		return soundPathText

	a = megagod.generateGod()
	videoPathText = random_video()
	soundPathText = random_sound()
	print('hellooooo')
	print(videoPathText)
	print(soundPathText)
	return render_template('index.html', sacredText=a, videoPath=videoPathText, soundPath = soundPathText)
