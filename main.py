from interaction_control import *
from game import *

class Simon:

    def __init__(self):
        self.interaction = Interaction()
        self.interaction.components['robot'] = RobotNao(self.interaction, 'robot')
        self.interaction.components['child_kinect'] = ChildKinect(self.interaction, 'child_kinect')
        self.interaction.components['game'] = GameManager(self.interaction, 'game')

        self.interaction.load(filename='./game/transitions_simon_says.json')
        self.interaction.next_interaction()


        self.interaction.components['game'].start()
        self.interaction.components['child_kinect'].start()
        self.interaction.components['robot']

simon = Simon()
while True:
    pass