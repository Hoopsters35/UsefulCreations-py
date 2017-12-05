import random, shelve

morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--',
'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..', 
'1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----'}

dict = shelve.open('UsefulDictionaries')
dict['morseCode'] = morse
dict.close()

# shuffle morse
keys = list(morse.keys())
random.shuffle(keys)


#keep track of number correct
numCorrect = 0

# print question and check answer
for key in keys:

	# choose randomly between key and value
	keyOrVal = random.randint(0,1)
	if keyOrVal == 0:
		print('What is', key, 'in Morse Code? ')
		inp = input()
		if inp == morse[key]:
			print('Correct!')
			numCorrect += 1
		else:
			print('Incorrect.', key, 'in Morse Code is', morse[key])

	if keyOrVal == 1:
		print('What is', morse[key], 'in Morse Code? ')
		inp = input()
		if inp == key:
			print('Correct!')
			numCorrect += 1
		else:
			print('Incorrect.', morse[key], 'in Morse Code is', key)

#TODO: print final score and questions missed
print("End of test\nYou got", numCorrect, "out of 36 correct. That's " + str(100*numCorrect//36) + "%")