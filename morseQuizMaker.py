import os, shelve, random

#get the morse code values off the shelf
shelf = shelve.open('UsefulDictionaries')
morse = shelf['morseCode']
keys = list(morse.keys())
shelf.close()

#write files to this directory
os.chdir('Morse Code Quizzes')

#get number of quizzes to create:
numFiles = int(input('How many Morse Code quizzes would you like to create? '))

#make x number of quizzes
for i in range(numFiles):
	#create quiz file
	quizName = 'quiz{0}.txt'.format((i + 1))
	quiz = open(quizName, 'w')
	header = "Name: \n\nDate: \n\nClass: \n\n" + " "*20 + "Morse Code Quiz\n\n"
	quiz.write(header)

	#create answerkey file
	answerkeyName = 'quiz{0}key.txt'.format((i + 1))
	answerkey = open(answerkeyName, 'w')
	#write to quiz/answer file

	random.shuffle(keys)
	qnum = 1
	for key in keys:
		keyOrVal = random.randint(0,1)
		if keyOrVal == 0:
			quizLine = '{0}) What is {1} in Morse Code?\n\n'.format(qnum, key)
			quiz.write(quizLine)
			ansLine = '{0}) {1}\n'.format(qnum, morse[key])
			answerkey.write(ansLine)
		elif keyOrVal == 1:
			quizLine = '{0}) What is {1} in Morse Code?\n\n'.format(qnum, morse[key])
			quiz.write(quizLine)
			ansLine = '{0}) {1}\n'.format(qnum, key)
			answerkey.write(ansLine)
		qnum += 1
	quiz.close()
	answerkey.close()
	#done making quizzes
print(numFiles, ' quizzes and answer keys made in', os.getcwd())
