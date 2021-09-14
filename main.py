from Battleground import *
from Wizard import *

# main function
if __name__ == '__main__':
    # creating battleground object
    b = Battleground()

    # reading spells from file
    b.read_spells()

    # main game loop
    while b.game_on():
        # main battle function
        b.battle()
        # print each players details
        b.print_data()

    # print the winner at the end
    b.print_winner()