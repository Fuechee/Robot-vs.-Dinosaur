import random
from weapon import Weapon

wp1 = Weapon('Double X"s Satelite Cannon', 100)
wp2 = Weapon('Trans-Am Raiser Sword', 75)
wp3 = Weapon('Plasma Rifle', 30)

weapon_list = [wp1, wp2, wp3]

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = random.choice(weapon_list)
    
    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power


       
        

