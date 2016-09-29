from interaction_control import *
from game import *
from Nao import *
import random
import time

class Simon:

    def __init__(self):
        self.interaction = Interaction()
        self.interaction.components['robot'] = RobotNao(self.interaction, 'robot')
        self.interaction.components['robot'].robot = NaoNode()
        self.interaction.components['child_kinect'] = ChildKinect(self.interaction, 'child_kinect')
        self.interaction.components['game'] = GameManager(self.interaction, 'game')

        self.interaction.load(filename='./game/transitions_simon_says.json')
        self.interaction.next_interaction()

        self.howie = self.interaction.components['robot'].robot

    def robot_performs_action(self):
        self.pose_selected = random.choice(self.howie.pose_names)
        print('selected: ', self.pose_selected)

        self.hertzel_says = random.choice([True, False])
        if self.hertzel_says == True:
            self.howie.play_file('Hertzel says.wav')
        wav_file = self.pose_selected.replace('_', ' ') + '.wav'
        print(wav_file)
        self.howie.play_file(wav_file)

        self.howie.move_to_pose(self.howie.poses[self.pose_selected])
        self.state = 'waiting'


simon = Simon()

simon.interaction.components['game'].start()
simon.interaction.components['child_kinect'].start()
simon.interaction.components['child_kinect'].current_state = 'wait_for_current_pose'

simon.howie.move_to_pose(simon.howie.base_pose)

for a in range(10):
    simon.robot_performs_action()
    simon.internal_clock = 10
    while simon.state == 'waiting':
        time.sleep(0.5)
        if simon.interaction.components['child_kinect'].current_state == 'received_pose':
            indices = simon.interaction.components['child_kinect'].current_param
            pose_detected_names = []
            for i, ind in enumerate(indices):
                if ind:
                    pose_detected_names.append(simon.howie.pose_names[i])
            print(simon.pose_selected, 'The poses', pose_detected_names)
            if simon.pose_selected in pose_detected_names:
                if simon.hertzel_says == True:
                    simon.howie.play_file('after Hertzel says+ currect child move 2  OR after NO Hertzel says+ child not moved.wav')
                    print('correct pose')
                else:
                    simon.howie.play_file('after NO Hertzel says+ child move.wav')
                    print('Got you!')
                break
            else:
                print('wrong pose')
                simon.interaction.components['child_kinect'].current_state = 'wait_for_current_pose'
        simon.internal_clock -= 1
        if simon.internal_clock == 0:
            if simon.hertzel_says == True:
                simon.howie.play_file('after Hertzel says+ wrong child move.wav')
                print('I said Simon says, you didnt get it')
            else:
                simon.howie.play_file('after Hertzel says+ currect child move 4 OR after NO Hertzel says+ child not moved.wav')
                print('goob job, didnt fool you')
            break




    # simon.interaction.components['robot'].start_pose_detection()
    # simon.interaction.components['child_kinect'].wait_for_start_pose()
    #
    #
    #
    # while True:
    #     if simon.interaction.components['child_kinect'].current_state == 'start_pose_detected':
    #         simon.interaction.components['robot'].introduction()
    #         simon.interaction.components['child_kinect'].wait_for_yes_pose()
    #     if simon.interaction.components['child_kinect'].current_state == 'yes_pose_detected':
    #         print('end')
    #     pass\

