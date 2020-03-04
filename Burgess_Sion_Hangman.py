import random #To create the random word
import time #To allow for pause to display beginning and end messages
guessedletters=[] #Blank variable to put player's guessed letters into
incorrect=[] #Blank variable to put player's incorrectly guessed letters into

#Creates a random word by using the random module and the wordlist
rawlist=("rarely universe notice sugar interference constitution we minus breath clarify take recording amendment hut tip logical cast title brief none relative recently detail port such complex bath soul holder pleasant buy federal lay currently saint for simple deliberately means peace prove sexual chief department bear injection off son reflect fast ago education prison birthday variation exactly expect engine difficulty apply hero contemporary that surprised fear convert daily yours pace shot income democracy albeit genuinely commit caution try membership elderly enjoy pet detective powerful argue escape timetable proceeding sector cattle dissolve suddenly teach spring negotiation solid seek enough surface small search ")
editlist = rawlist.split() #Divides the entire string of words on the list into seperate, individual words
wordlist= editlist #Wordlist becomes the list of seperated words
gameword=(wordlist[random.randint(0,len(wordlist)-1)]) #Selects a word from the wordlist
attempts=7 #Only 7 attempts are allowed

print("Are you ready to play...") #A welcome statement
print("  ----¬\n  |   |\n  O   |\n /|\  |\n  |   |\n / \  |\n      | \n ------\n \nHangman? ")

while attempts != 0: #The While Loop removes lives off player for incorrect answers and reveals letters for correct answers. Also produces an error if they try and enter more than one character like a numpty
	secretword = ""  #Blank space for string
	for letter in gameword: 
		if letter in guessedletters:  #The If & Else loop shows/hides the letters that have been guessed
			secretword = secretword + letter
		else:
			secretword = secretword + "*"
	if secretword == gameword: #This ends the loop if all letters of the gameword have been guessed correctly
		break
	print(secretword)
	print("\nPlease enter your next guess: ")
	print(attempts, "lives left")

	guess = input() #Player inputs a letter

	if guess in guessedletters or guess in incorrect: #This informs the player they have already guessed the letter
		print("You've already guessed that letter!")
	elif len(guess) > 1: #Informs the player they have entered more than one character.  An illegal move and deeply frowned upon in the world of hangman.
		print("One letter at a time please you absolute nutter!")
	elif guess in gameword:
		guessedletters.append(guess) #This adds the players guess into the already guessed letters with a spot of positive reinforcement, which can go a long way for morale.
		print("\n \n \n \nSpot on, that letter is correct! You have guessed", guessedletters, "correctly, and ",incorrect, "incorrectly")
	else:
		print("I'm afraid that letter isn't in the word my friend!")
		attempts -= 1 #Removes a life off the player
		incorrect.append(guess)
		print("\n \n \n \nUnlucky me old fruit. That letter isn't in the word.  You have guessed", guessedletters, "correctly, and ",incorrect, "incorrectly")
	print()

if attempts:
	print("\n\n\nCongratulations, you win!")
	print("  ----¬\n      |\n      |\n  O   |\n \|/  |\n  |   |\n / \  |\n ------")
	print("\nThe answer was", gameword)
	time.sleep(15) #Allows time for message to be displayed
else:
	print("You lose!")
	print("  ----¬\n  |   |\n  O   |\n /|\  |\n  |   |\n / \  |\n      | \n ------")
	print("The correct answer was", gameword)
	time.sleep(15) #Allows time for message to be displayed