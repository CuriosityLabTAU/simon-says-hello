from interaction_control.component import *
import rospy
import random
#import String


class GameManager(Component):
    #kinect_listener = None

    def start(self):
        print('Starting GameManager')
        self.current_state = 'started'

    def start_game(self):
        print('starting game')
        self.current_param = "both_hands_up"

    def choose_action(self):
        param = random.randint(0, 12)
        self.current_param = param
        print self.current_param
        self.current_state = "got_action"

    def wait(self):
        pass

    def request_pose(self):
        pass

    def judge_pose(self):
        pass
