from interaction_control import *
from game import *
from Nao import *

class Simon:

    def __init__(self):
        self.interaction = Interaction()
        self.interaction.components['robot'] = RobotNao(self.interaction, 'robot')
        self.interaction.components['robot'].robot = NaoNode()
        self.interaction.components['child_kinect'] = ChildKinect(self.interaction, 'child_kinect')
        self.interaction.components['game'] = GameManager(self.interaction, 'game')

        self.interaction.load(filename='./game/transitions_simon_says.json')
        self.interaction.next_interaction()


simon = Simon()

simon.interaction.components['game'].start()
simon.interaction.components['child_kinect'].start()
simon.interaction.components['robot'].start_pose_detection()
simon.interaction.components['child_kinect'].wait_for_start_pose()



while True:
    if simon.interaction.components['child_kinect'].current_state == 'start_pose_detected':
        simon.interaction.components['robot'].introduction()
        simon.interaction.components['child_kinect'].wait_for_yes_pose()
    if simon.interaction.components['child_kinect'].current_state == 'yes_pose_detected':
        print('end')
    pass