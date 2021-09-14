class Wizard:
    _health = 100
    _energy = 500
    _shield = 3
    _spells = {}
    def __init__(self, name):
        self._name = name

    def add_spell(self, spellname, spellpower):
        self._spells[spellname] = int(spellpower)
    
    @classmethod
    def add_spell_to_all(cls, spellname, spellpower):
        cls._spells[spellname] = int(spellpower)

    def get_name(self):
        return self._name
    
    def get_health(self):
        return self._health

    def get_energy(self):
        return self._energy

    def has_shield(self):
        return self._shield > 0

    def use_shield(self):
        self._shield-=1

    def select_spell(self, spellname):
        spell = self._spells.get(spellname)
        if spell == None:
            return -1

        if spell > self._energy:
            return -2
        else:
            self._spell = spell
            return spell

    def confirm_spell(self):
        if self._shield_selected:
            self.use_shield()
            return 0
        else:
            self._energy -= self._spell
            return self._spell

    def select_shield(self):
        self._shield_selected = 1

    def reset_spells(self):
        self._shield_selected = 0
        self._spell = None

    def take_damage(self, damage):
        if damage <= 0:
            return
        self._health -= damage
        if self._health < 0:
            self._health = 0

    def print_spells(self):
        print(self._spells)