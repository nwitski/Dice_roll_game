
import sys
from random import randint



print ('hello there, I have a dice with 6 sides, how many times can you get it right in 10 tries? \n')


#define user answer
user_answer = "y"


#continue the game
while (user_answer.lower() == "y"):
	turns = 10
	correct_guesses = 0
	random_guess = randint(1,6)

	# game mechanics begin for turns being greater than 0
	while turns > 0:

		# defining outliers above 6 and below 1
		user_guess = int(input('Guess a number on a die: '))
		if 0 > user_guess or user_guess >= 7:
			print ('That is not a valid imput')


		turns = turns - 1


		# definining the conditions if the user wins or loses
		if user_guess != random_guess:
			print ('You have %s guesses left' % turns)
		if user_guess == random_guess:
			correct_guesses = correct_guesses + 1


			# how many times did the user get it right
			if correct_guesses == 1:
				print ('you got it right %s time' % correct_guesses)
			else:
				print ('you got it right %s times' % correct_guesses)
			random_guess = randint(1,6)


	# finishing the loop and quitting the operation
	user_answer = str(input('want to play? (y/n): '))
	if (user_answer.lower() == "n"):
		sys.quit()

	




