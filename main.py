from Battleground import *
from Wizard import *

if __name__ == '__main__':
    b = Battleground()
    b.read_spells()
    while b.game_on():
        b.battle()
        b.print_data()
    b.print_winner()