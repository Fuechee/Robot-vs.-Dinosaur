from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()
    
    def run_game(self):
        self.display_welcome(self)
        self.battle_phase(self)
        self.display_winner(self)


    def display_welcome(self):
        pass

    def battle_phase(self):
        pass

    def display_winner(self):
        if len(self.robot) == 0:
            print('')
        