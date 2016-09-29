from interaction_control import *
from game import *

class Simon:

    def __init__(self):
        self.interaction = Interaction(
            [('robot', 'RobotNao'),
             ('child_kinect', 'ChildKinect')
             ]
        )
        self.interaction.components['robot'] = RobotNao(self.interaction, 'robot')
        self.interaction.components['child_kinect'] = ChildKinect(self.interaction, 'child_kinect')

        self.interaction.load(filename='./game/transitions_simon_says.json')
        self.interaction.next_interaction()
