from interaction_control import *

class RobotNao(Component):
    talk_node = None
    act_node = None
    robot = None

    def introduction(self):
        self.current_state = 'introduction'
        self.robot.play_file('intro.wav')

    def act(self, action):
        self.current_param = action
        self.current_state = "act"
        # say saimon says
        print "Simon says", self.current_param
        # say raise you hands
        print "raise you hands"
        # raise robot hands
        print "raising hands"
        self.current_state = "finished_action"

    def respond(self):
        pass

    def start_pose_detection(self):
        self.robot.play_file('hello.wav')





