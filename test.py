import random

# Function to play the number guessing game
def play_game():
    number_to_guess = random.randint(1, 100) #Generate a random number between 1 and 100
    attempts = 0
    print('Welcome to the Number Guessing Game!')
    print('I have selected a number between 1 and 100. Try to guess it.')
    while True:
        # try:
            guess = int(input('Enter your guess: ')) #Get the user's guess
            attempts += 1
            if guess < number_to_guess:  #Check if the guess is too low
                print('Too low! Try again.')
            elif guess > number_to_guess: #Check if the guess is too high
                print('Too high! Try again.')
            else: #The guess is correct
                print(f'Congratulations! You guessed the number correctly in {attempts} attempts.')
                break
        # except ValueError: #Check if the input is an integer
            # print('Invalid input. Please enter an integer.')

# Main program      
while True:
    play_game()
    play_again = input('Do you want to play again? (yes/no): ').strip().lower() #Ask the user if they want to play again
    if play_again in ['yes','y']: #Check if the user wants to play again
        play_game()
    elif play_again in ['no','n']: 
        print('Thank you for playing! Goodbye!')
        break
    else:
        print('Invalid input. Please enter "yes" or "no".')        
