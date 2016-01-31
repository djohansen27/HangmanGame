#Hangman by David Johansen
#CS 2450
#making a change - another change

word = "Salt Lake"
brokenUpWord = []
underscores = []

for char in word:
	brokenUpWord.append(char)

#populating the array with underscores
for char in brokenUpWord:
	if char == " ":
		underscores.append(" ")
	else:
		underscores.append("_")

#check if all the letters in the word have been guessed, if not continue
def checkStatus():
	index=0
	for char in underscores:
		if underscores[index].lower() != brokenUpWord[index].lower():
			correct = 0
			return
		else:
			correct = 1
		index+=1

	if correct == 1:
		print "Congratulations, you guessed the word!"
		exit()

#Drawing hangman and printing lives
def drawHangman(lives, underscores):
	if lives == 6:
		print "you have %d" % lives + " lives\n"
		print " -----"
		print " |   |"
		print " |"
		print " |"
		print " |"
		print " |"
		print "=====\n"
		print " ".join(underscores)
	elif lives == 5:
		print "you have %d" % lives + " lives\n"
		print " -----"
		print " |   |"
		print " |   O"
		print " |"
		print " |"
		print " |"
		print "=====\n"
		print " ".join(underscores)
	elif lives == 4:
		print "you have %d" % lives + " lives\n"
		print " -----"
		print " |   |"
		print " |   O"
		print " |  /"
		print " |"
		print " |"
		print "=====\n"
		print " ".join(underscores)
	elif lives == 3:
		print "you have %d" % lives + " lives\n"
		print " -----"
		print " |   |"
		print " |   O"
		print " |  /|"
		print " |"
		print " |"
		print "=====\n"
		print " ".join(underscores)
	elif lives == 2:
		print "you have %d" % lives + " lives\n"
		print " -----"
		print " |   |"
		print " |   O"
		print " |  /|\\"
		print " |"
		print " |"
		print "=====\n"
		print " ".join(underscores)
	elif lives == 1:
		print "you have %d" % lives + " lives\n"
		print " -----"
		print " |   |"
		print " |   O"
		print " |  /|\\"
		print " |  /"
		print " |"
		print "=====\n"
		print " ".join(underscores)
	elif lives == 0:
		print "you have %d" % lives + " lives\n"
		print " -----"
		print " |   |"
		print " |   O"
		print " |  /|\\"
		print " |  / \\"
		print " |"
		print "=====\n"
		print " ".join(underscores)

#Accept letter input. Check to see if it's right
def game():
	print "Welcome to hangman! Try to guess the letters in the word."
	lives=6
	guess=""
	drawHangman(lives, underscores)
	while lives !=0:
		guess = raw_input("\nYour guess: ")
		index=0
		lostlife=1
		for char in brokenUpWord:
			if char.lower() == guess.lower():
				underscores[index]=guess
				lostlife=0
			index+=1
		if lostlife == 1:
			lives-=1
			print "That letter is not in the word"
			drawHangman(lives, underscores)
		else:
			print "Good job! You discovered a letter"
			drawHangman(lives, underscores)
		checkStatus()

game()

print "\nI'm sorry, you lost"



