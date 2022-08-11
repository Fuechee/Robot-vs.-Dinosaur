from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot('Orix')
        self.dinosaur = Dinosaur('Godzilla', 35)
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()


    def display_welcome(self):
        print('\nWelcome to Robot VS Dinosaur\nWho will Win!\n')

    def battle_phase(self):
        while(self.robot.health >0 and self.dinosaur.health >0):
            self.robot.attack(self.dinosaur)
            print(f'{self.robot.name} attacked {self.dinosaur.name} with {self.robot.active_weapon.name} for {self.robot.active_weapon.attack_power} damage!!')
            print(f'{self.dinosaur.name} has {self.dinosaur.health} health remaining!')
            if(self.dinosaur.health >0):
                self.dinosaur.attack(self.robot)
                print(f'{self.dinosaur.name} attacked {self.robot.name} for {self.dinosaur.attack_power} damage!!!')
                print(f'{self.robot.name} has {self.robot.health} health remaining!')

    def display_winner(self):
        if(self.robot.health <= 0):
            print(f'{self.dinosaur.name} is the WINNER!!!')
        elif(self.dinosaur.health <= 0):
            print(f'{self.robot.name} is the WINNER!!!!')
            