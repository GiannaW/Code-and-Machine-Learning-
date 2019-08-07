import random

class BattleBot:
    def __init__(self, name):
        self.name = name
        self.health = 100.0
        self.defense = 10.0
        self.attack = 10.0
        self.speed = 10.0

    def is_alive(self):

        if self.health <= 0:
            return False
        else:
            return True

    def _attack(self, opponent):
        damage_dealt = self.attack + (self.attack * (opponent.defense / 100))
        opponent.take_damage(damage_dealt)

    def take_damage(self, damage_dealt):
        self.health -= damage_dealt

    def build_attack(self):
        self.defense -= 1
        self.attack += 2
        self.speed -= 1

    def build_defense(self):
        self.defense += 2
        self.attack -= 1
        self.speed -= 1

    def build_speed(self):
        self.defense -= 1
        self.attack -= 1
        self.speed += 2

    def build_health(self):
        self.defense -= 1
        self.attack -= 1
        self.speed -= 1
        self.health += 5

    def get_stats(self):
        print(self.name)
        print("*\tHealth: " + str(self.health))
        print("*\tAttack: " + str(self.attack))
        print("*\tDefense: " + str(self.defense))
        print("*\tSpeed: " + str(self.speed))
    def action(self, opponent):
        random_num = random.randint(0, 100)
        if (random_num <= 20):
            self.build_defense()
        elif random_num <= 40:
            self.build_attack()
        elif self.health <= 50:
            self.build_health()
        elif random_num <= 60:
            self.build_speed()
        elif random_num <= 90:
            self._attack(opponent)



        else:
            print(self.name + " has chosen to take this opportunity to study his opponent.")


class BattleBot2:
    def __init__(self, name):
        self.name = name
        self.health = 100.0
        self.base_armor = 10.0
        self.base_damage = 10.0
        self.speed = 10.0

    def attack(self, opponent):
        damage_dealt = self.base_damage - (self.base_damage * (opponent.base_armor / 100))
        opponent.take_damage(damage_dealt)

    def take_damage(self, damage_dealt):
        self.health -= damage_dealt

    def build_armor(self):
        self.base_armor += 2
        self.base_damage -= 1
        self.speed -= 1

    def build_attack(self):
        self.base_armor -= 1
        self.base_damage += 2
        self.speed -= 1

    def build_speed(self):
        self.base_armor -= 1
        self.base_damage -= 1
        self.speed += 2

    def is_alive(self):
        if self.health <= 0:
            return False
        else:
            return True

    def get_stats(self):
        print(self.name)
        print("Health:  + str(self.health")
        print("Attack: + str(self.base_damage")
        print("Defense: + str(self.base_armor")
        print("Speed:" + str(self.speed))

    def action(self, opponent):
        random_number = random.randint(0, 100)
        if (random_number <= 20):
            self.build_armor()
        elif (random_number <= 40):
            self.build_attack()
        elif (random_number <= 60):
            self.build_speed()
        elif (random_number <= 90):
            self.attack(opponent)
        else:
            print(self.name + " glitched out!")


class Arena:
    def __init__(self, Bot1, Bot2):
        self.bbot1 = Bot1
        self.bbot2 = Bot2

    def battle(self):
        while self.bbot1.is_alive() and self.bbot2.is_alive():
            # begin battle round
            if self.bbot1.speed <= self.bbot2.speed:
                self.bbot1.action(self.bbot2)
                self.bbot2.action(self.bbot1)
                self.bbot1.get_stats()
                self.bbot2.get_stats()
                input("Press Enter fot the Next Round")
            else:
                self.bbot2.action(self.bbot1)
                self.bbot1.action(self.bbot2)
                self.bbot2.get_stats()
                self.bbot1.get_stats()
                input("Press Enter for the Next Round")
        if self.bbot1.is_alive():
            print(self.bbot1.name + " is the winner!")
        else:
            print(self.bbot2.name + " is the winner!")


