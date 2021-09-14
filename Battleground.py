from Wizard import *

class Battleground:
    def __init__(self):
        self._wizards = [Wizard('Harry'), Wizard('Voldemort')] # create wizards 
        self._game = True # flag to note wether game ended or not


    def battle(self): # main battle method
        user_input = input('Enter the two spells (harry then voldemort): ').split(' ') # read user input and split it to 2 spells
        if len(user_input) != 2: # if input isnt exactly 2 words print error and stop 
            print('Invalid input!')
            return
        
        for wizard, string in zip(self._wizards, user_input): # looping through input and wizards
            wizard.reset_spells() # reset spells used in last round
            
            attack = wizard.select_spell(string) # selecting spell with user input

            # handling special cases
            if attack == 0 and not wizard.has_shield(): # if user selected sheild and hes out of sheilds
                print(wizard.get_name() + ' is out of shields!')
            elif attack == -1: # if spell ios not found
                print('Invalid spell entered for ' + wizard.get_name() + '!')
            elif attack == -2: # if energy isnt sufficient
                print(wizard.get_name() + ' doesnt have enough energy for this attack!')
        
        attack = [wizard.confirm_spell() for wizard in self._wizards] # confirming spells for both wizards

        if -1 in attack: # if any of them used a sheild then none of them will take damage
            return
        else: # else both of them will take damage equal to the difference of attacks and if that number is negative it will not be applied
            self._wizards[0].take_damage(attack[1] - attack[0])
            self._wizards[1].take_damage(attack[0] - attack[1])

        # check if either of them has 0 health
        if self._wizards[0].get_health() == 0:
            self._winner = self._wizards[1]
            self._game = False
        elif self._wizards[1].get_health() == 0:
            self._winner = self._wizards[0]
            self._game = False

    # method to read spells from file
    def read_spells(self):
        f = open("spells.txt", mode="r")
        lines = f.readlines()
        for line in lines:
            components = line.split(' ')
            if len(components) != 3: # if there arent exactly 3 components in a spell it is not correct
                continue
            wiz, name, power = components
            if wiz == 'H':
                self._wizards[0].add_spell(name, power)
            elif wiz == 'V':
                self._wizards[1].add_spell(name, power)
            elif wiz == 'A':
                Wizard.add_spell_to_all(name, power)

        f.close()

    #method to print current battle details
    def print_data(self):
        print('\t' + self._wizards[0].get_name() + '\t\t\t' + self._wizards[1].get_name())
        print('Health : ' + str(self._wizards[0].get_health()) + '\t\t\t' + str(self._wizards[1].get_health()))
        print('Energy : ' + str(self._wizards[0].get_energy()) + '\t\t\t' + str(self._wizards[1].get_energy()))

    # getter to check if game ended
    def game_on(self):
        return self._game

    #method to print winner
    def print_winner(self):
        print('\t' + self._winner.get_name() + ' is the winner ..')

        