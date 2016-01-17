# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

num_range = 100

    # helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    if num_range == 100:
        range100();
    elif num_range == 1000:
        range1000()   
        
    # define event handlers for control panel   
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    global secret_number
    secret_number = random.randrange(0,100)
    print " "
    print "New game. Range is from 0 to 100"
    global number_left 
    number_left = 7
    print "Number of remaining guesses is", number_left


def range1000():
    # button that changes the range to [0,1000) and starts a new game  
    global num_range
    num_range = 1000
    global secret_number
    secret_number = random.randrange(0,1000)
    print " "
    print "New game. Range is from 0 to 1000"
    global number_left
    number_left = 10
    print "Number of remaining guesses is", number_left
    
def input_guess(guess):
    guess = int(guess)
    print " "
    global number_left
    print "Guess was", guess
    number_left -= 1
    print "Number of remaining guesses is", number_left
    if number_left == 0:
        if guess != secret_number:
            print"You ran out of guesses. The number was", secret_number
            return new_game()
        else:
            print "Correct!"
            return new_game()
    
    if guess > secret_number:
        print "Lower!"
    elif guess < secret_number:
        print "Higher!"
    else:
        print "Correct!"
        return new_game()
    
    
    
# create frame
f = simplegui.create_frame ("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()



