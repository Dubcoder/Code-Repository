from random import randint

# In this project, the player will be playing a game of Rock, Paper, Scissors

name = raw_input("What's your name? ")
def rock_paper_scissors():
    player_choice = raw_input("Rock (r), Paper (p), or Scissors (s): ")
    while player_choice != "r" and player_choice != "p" and player_choice != "s":
        player_choice = raw_input("Sorry, I didn't catch that. Please re-enter your choice. " \
                                  "Rock (r), Paper (p), Scissors (s): ")
    print "%s vs." % player_choice
    computer_choice = randint(1, 3)
    if computer_choice == 1:
        print "r"
    elif computer_choice == 2:
        print "p"
    elif computer_choice == 3:
        print "s"
    if player_choice == "r" and computer_choice == 1:
        print "DRAW"
    elif player_choice == "p" and computer_choice == 2:
        print "DRAW"
    elif player_choice == "s" and computer_choice == 3:
        print "DRAW"
    elif player_choice == "r" and computer_choice == 2:
        print "Computer Wins!"
    elif player_choice == "r" and computer_choice == 3:
        print "%s Wins!" % name
    elif player_choice == "p" and computer_choice == 1:
        print "%s Wins!" % name
    elif player_choice == "p" and computer_choice == 3:
        print "Computer Wins!"
    elif player_choice == "s" and computer_choice == 1:
        print "Computer Wins!"
    elif player_choice == "s" and computer_choice == 2:
        print "%s Wins!" % name
rock_paper_scissors()