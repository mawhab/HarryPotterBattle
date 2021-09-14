from Wizard import *

class Battleground:
    def __init__(self):
        self._wizards = [Wizard('Harry'), Wizard('Voldemort')]
        self._game = True


    def battle(self):
        user_input = input('Enter the two spells (harry then voldemort): ').split(' ')
        if len(user_input) < 2:
            print('Invalid input!')
            return
        
        for wizard, string in zip(self._wizards, user_input):
            wizard.reset_spells()
            if string == 'shield':
                if wizard.has_shield():
                    wizard.select_shield()
                else:
                    print(wizard.get_name() + ' is out of shields!')
                    return
            else:
                attack = wizard.select_spell(string)
                if attack == -1:
                    print('Invalid spell entered for ' + wizard.get_name() + '!')
                    return
                elif attack == -2:
                    print(wizard.get_name() + ' doesnt have enough energy for this attack!')
                    return
        
        attack = [wizard.confirm_spell() for wizard in self._wizards]

        if 0 in attack:
            return
        else:
            self._wizards[0].take_damage(attack[1] - attack[0])
            self._wizards[1].take_damage(attack[0] - attack[1])

        if self._wizards[0].get_health() == 0:
            self._winner = self._wizards[1]
            self._game = False
        elif self._wizards[1].get_health() == 0:
            self._winner = self._wizards[0]
            self._game = False

    def read_spells(self):
        f = open("spells.txt", mode="r")
        lines = f.readlines()
        for line in lines:
            wiz, name, power = line.split(' ')
            if wiz == 'H':
                self._wizards[0].add_spell(name, power)
            elif wiz == 'V':
                self._wizards[1].add_spell(name, power)
            elif wiz == 'A':
                Wizard.add_spell_to_all(name, power)

        f.close()

    def print_data(self):
        print('\t\t' + self._wizards[0].get_name() + '\t\t' + self._wizards[1].get_name())
        print('Health : ' + str(self._wizards[0].get_health()) + '\t\t\t' + str(self._wizards[1].get_health()))
        print('Energy : ' + str(self._wizards[0].get_energy()) + '\t\t\t' + str(self._wizards[1].get_energy()))

    def game_on(self):
        return self._game

    def print_winner(self):
        print('\t' + self._winner.get_name() + ' is the winner ..')

        