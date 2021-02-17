# Forge is a novel writing app that takes inputted research texts, dates, and other features 
# to create a novel
import random
import nltk
from nltk import sent_tokenize


# date class uses random to choose a day, month, and year. Year range will be inputted in app

class date:
		day = (random.randrange(1, 28))
		month = ["January", "February", "March", "April", ]
		randomMonth = random.choice(month)
		year = (random.randrange(1805, 1830))
		print(str(day) + " " + randomMonth + " " + str(year))

#weather class uses random weather and time to set scene

class weather:
	weather = ["cloudy", "dark", "light", "red", "black", "heavy", "wet", "airy", "cold", "damp", "blustery","freezing"]
	randomWeather = random.choice(weather)
	time = ["day", "night", "evening", "afternoon", "twilight", "morning", "early morning"]
	randomTime = random.choice(time)
	print("The " + randomTime + " was " + randomWeather + ".")


class opening:
	opening = ["Strange thoughts fill my mind.", "Snatches of books come to me.", "My mind is awash with words."]
	randomOpening = random.choice(opening)
	print(randomOpening)


# class converts txt file into string, gets length, then uses random function to 
# pick point and write out 75 characters. Text file will be inputted in app (or 
# choose from range).

class bolivarSpeeches:
	with open ("bolivarSpeeches.txt", "r") as file:
		bolivarSpeeches = file.read()
		bolivarSpeechesLen = (len(bolivarSpeeches))
		randomIndex = (random.randrange(1, bolivarSpeechesLen))
		for x in range(1, 75, 1):
			print (bolivarSpeeches[randomIndex + x], end ='', sep='')


class humboldtAmericas:
	with open ("humboldtAmericas.txt", "r") as file:
		humboldtAmericas = file.read()
		humboldtAmericasLen = (len(humboldtAmericas))
		randomIndex = (random.randrange(1, humboldtAmericasLen))
		for x in range(1, 75, 1):
			print (humboldtAmericas[randomIndex + x], end ='', sep='')


class oConnellSpeeches:
	oConnellSpeeches = open("oConnellSpeeches.txt").read()
	sentences = nltk.sent_tokenize(oConnellSpeeches)
	randomSentence = random.choice(sentences)
	print (randomSentence)


class oConnellSpeechesGeneration:
	file = open("oConnellSpeeches.txt", "r")
	text = file.read()
	text1=text.split()
	oConnellSpeeches=nltk.Text(text1)
	oConnellSpeeches.generate()





		

