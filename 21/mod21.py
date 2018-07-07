class Equipment:

    def __init__(self, name, cost, damage, armour):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armour = armour

    def __str__(self):
        return f"{self.name}, {self.cost}, {self.damage}, {self.armour}"


class Fighter:

    def __init__(self, name, health, damage, armour, equipment=list()):
        self.name = name
        self.health = health
        self.damage = damage
        self.armour = armour
        self.goldspent = 0
        self.equipment = list()
        for i in equipment:
            self.equipment.append(i)
            self.goldspent += i.cost
            self.damage += i.damage
            self.armour += i.armour


def get_damage(damage, armour):
    if damage > armour:
        return (damage - armour)
    else:
        return 1


def fight(fighter1, fighter2):
    winner = None
    while not winner:
        fighter2.health -= get_damage(fighter1.damage, fighter2.armour)
        if fighter2.health <= 0:
            winner = fighter1
        else:
            fighter1.health -= get_damage(fighter2.damage, fighter1.armour)
            if fighter1.health <= 0:
                winner = fighter2
    return winner
