import random

def guess(x):
  random_number = random.randint(1,x)
  guess = 0
  while guess != random_number:
    guess = int(input("Enter a number: "))
    if guess < random_number:
      print('Sorry, guess again. Too low.')
    elif guess > random_number:
      print('Too high.')
#guess(10)

def computer_guess(x):
	low = 1
	high = x
	feedback = ""
	while feedback != 'c':
		if low != high:
			guess = random.randint(low, high)
		else:
			guess = low
		feedback = input('Is {} too high, too low, or correct'.format(guess)).lower()
		if feedback == 'h':
			high = guess - 1
		elif feedback == 'l':
			low = guess + 1
	print('Yaay, the computer guessed your number {}'.format(guess))
computer_guess(10)
