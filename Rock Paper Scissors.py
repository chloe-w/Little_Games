import random

def name_to_number(name):
    if name == "rock":
        name = 0
        return name
    
    elif name == 'Spock':
        name = 1
        return name
    
    elif name == 'paper':
        name = 2
        return name
    
    elif name == 'lizard':
        name = 3
        return name
    
    elif name == 'scissors':
        name = 4
        return name
    
def number_to_name(number):
    if number == 0:
        number = "rock"
        return number
    
    elif number == 1:
        number = "Spock"
        return number
    
    elif number == 2:
        number = "paper"
        return number
    
    elif number == 3:
        number = "lizard"
        return number
    
    elif number == 4:
        number = "scissors"
        return number

def rpsls(player_choice): 
    print " "
    print "Player chooses", player_choice
    player_number = name_to_number(player_choice) 
    
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses", comp_choice
    
    rem = (player_number - comp_number) % 5
    if (rem == 1) or (rem == 2):
        print "Player wins!"
    elif (rem == 3) or (rem == 4):
        print "Computer wins!"
    elif rem == 0:
        print "Ties!"

    
# test!
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



