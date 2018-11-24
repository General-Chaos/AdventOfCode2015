import copy


class Fighter:

    def __init__(self, name, health, damage, armour):
        self.name = name
        self.health = health
        self.damage = damage
        self.__armour = armour
        self.effects = {}

    @property
    def armour(self):
        armour = self.__armour
        for k, v in self.effects.items():
            armour += v['armour']
        return armour

    def process_effects(self):
        effectstoremove = []
        for k, v in self.effects.items():
            self.health -= v['damage']
            v['timer'] -= 1
            if v['timer'] == 0:
                effectstoremove.append(k)
        for i in effectstoremove:
            del self.effects[i]


class Mage(Fighter):

    def __init__(self, name, health, damage, armour, mana):
        super().__init__(name, health, damage, armour)
        self.mana = mana
        self.manaspent = 0
        self.spellscast = []
        self.spells = {
            "magic_missile": {
                "damage": 4,
                "cost": 53,
                "heal": 0,
                "effect": {}
            },
            "drain": {
                "damage": 2,
                "cost": 73,
                "heal": 2,
                "effect": {}
            },
            "poison": {
                "damage": 0,
                "cost": 173,
                "heal": 0,
                "effect": {
                    "poison": {
                        "target": "boss",
                        "damage": 3,
                        "recharge": 0,
                        "armour": 0,
                        "timer": 6
                    }

                }
            },
            "shield": {
                "damage": 0,
                "cost": 113,
                "heal": 0,
                "effect": {
                    "shield": {
                        "target": "self",
                        "damage": 0,
                        "recharge": 0,
                        "armour": 7,
                        "timer": 6
                    }

                }
            },
            "recharge": {
                "damage": 0,
                "cost": 229,
                "heal": 0,
                "effect": {
                    "recharge": {
                        "target": "self",
                        "damage": 0,
                        "recharge": 101,
                        "armour": 0,
                        "timer": 5
                    }
                }
            }
        }

    def get_castable_spells(self, enemy):
        spells = []
        for k, v in self.spells.items():
            if v["cost"] <= self.mana:
                if v["effect"] == {}:
                    spells.append(k)
                else:
                    for j, l in v["effect"].items():
                        if l["target"] == "self":
                            if j in self.effects.keys():
                                pass
                            else:
                                spells.append(k)
                        else:
                            if j in enemy.effects.keys():
                                pass
                            else:
                                spells.append(k)
        return spells

    def process_effects(self):
        for k, v in self.effects.items():
            self.mana += v['recharge']
        super().process_effects()

    def cast_spell(self, enemy, spellname):
        spell = self.spells[spellname]
        enemy.health -= spell['damage']
        self.health += spell['heal']
        self.mana -= spell['cost']
        self.manaspent += spell['cost']
        for k, v in spell['effect'].items():
            if v['target'] == 'self':
                self.effects.update(copy.deepcopy(spell['effect']))
            else:
                enemy.effects.update(copy.deepcopy(spell['effect']))


def get_damage(damage, armour):
    if damage > armour:
        return (damage - armour)
    else:
        return 1


def get_victorious_mage_fights(mage, fighter, bestmana, mode='Normal'):
    if mode == 'Hard':
        healthgate = 6
    else:
        healthgate = 4
    if fighter.health <= 0:
        if mage.manaspent < bestmana:
            bestmana = mage.manaspent
        yield mage
    elif mage.health <= 0:
        pass
    else:
        # Mages turn
        if mode == 'Hard':
            mage.health -= 1
        fighter.process_effects()
        mage.process_effects()
        if mage.health <= 0:
            pass
        elif fighter.health <= 0:
            if mage.manaspent < bestmana:
                bestmana = mage.manaspent
            yield mage
        else:
            spells = mage.get_castable_spells(fighter)
            for i in spells:
                newmage = copy.deepcopy(mage)
                newfighter = copy.deepcopy(fighter)
                newmage.cast_spell(newfighter, i)
                newmage.spellscast.append(i)
                if newfighter.health <= 0:
                    if mage.manaspent < bestmana:
                        bestmana = mage.manaspent
                    yield newmage
                else:
                    # Fighters turn
                    newfighter.process_effects()
                    newmage.process_effects()
                    if newfighter.health <= 0:
                        if mage.manaspent < bestmana:
                            bestmana = mage.manaspent
                        yield newmage
                    else:
                        newmage.health -= get_damage(newfighter.damage, newmage.armour)
                        if newmage.health > 0 and mage.manaspent < bestmana and (newfighter. health / newmage.health) < healthgate:
                            yield from get_victorious_mage_fights(newmage, newfighter, bestmana, mode)
                        else:
                            pass
