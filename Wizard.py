class Wizard:
    # class variables with default value for all instances
    _health = 100
    _energy = 500
    _shield = 3
    _spells = {} # dictionary to store spells
    def __init__(self, name):
        self._name = name # initialize name only

    def add_spell(self, spellname, spellpower): # method to add spell to this instance only
        self._spells[spellname] = int(spellpower)
    
    @classmethod
    def add_spell_to_all(cls, spellname, spellpower): # class method to add spell to all instances
        cls._spells[spellname] = int(spellpower)

    # getters 
    def get_name(self):
        return self._name
    
    def get_health(self):
        return self._health

    def get_energy(self):
        return self._energy

    def has_shield(self):
        return self._shield > 0

    # method to use a sheild
    def use_shield(self):
        self._shield-=1

    #method to select a spell given the name
    def select_spell(self, spellname):
        spell = self._spells.get(spellname) # getting spell from dictionary
        if spell == None: # if spell given doesnt exist select no spell and return -1
            self._spell = 0
            return -1

        if spell == 0: # if spell is 0 that means its a sheild
            if self.has_shield(): # if there are remaining sheilds use one
                self.select_shield()
            else: # if there are none remaining select no spell
                self._spell = 0
            return 0

        if spell > self._energy: # if there isnt enough energy for this spell select nothing
            self._spell = 0
            return -2
        else: # if none of the above conditions apply select given spell and return its power
            self._spell = spell
            return spell

    def confirm_spell(self): # method to confirm the selected spell
        if self._shield_selected: # if sheild is selected use it
            self.use_shield()
            return -1
        else: # else use the given spell
            self._energy -= self._spell # reduce the spell energy
            return self._spell # and return its power

    def select_shield(self): # flag to keep track of wether or not a sheild is selected
        self._shield_selected = 1

    def reset_spells(self): # method to reset spells after each round
        self._shield_selected = 0
        self._spell = None

    def take_damage(self, damage): # method to reduce health by a given amount
        if damage <= 0: # if the damage is negative or 0 return
            return
        self._health -= damage
        if self._health < 0:
            self._health = 0
