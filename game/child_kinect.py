from interaction_control.component import *

import rospy
from std_msgs.msg import String

class ChildKinect(Component):
    kinect_listener = None

    def start(self):
        print('Starting kinect')
        self.current_state = 'started'

        rospy.init_node('kinect_listener', anonymous=True)
        rospy.Subscriber("kinect_poses", String, self.got_pose)
        # rospy.spin()

    def wait_for_start_pose(self):
        self.current_state = 'wait_for_start_pose'

    def wait_for_yes_pose(self):
        self.current_state = 'wait_for_yes_pose'

    def wait_for_current_pose(self):
        self.current_state = 'wait_for_current_pose'

    def wait(self):
        pass

    def got_pose(self, data):
        poses = eval(data.data)

        if self.current_state == 'wait_for_start_pose':
            print('check if poses is only start pose')
            if poses[2] == 1:
                self.current_state = 'start_pose_detected'
                return

        if self.current_state == 'wait_for_yes_pose':
            print('check if poses is only yes pose')
            if poses[0] == 1:
                self.current_state = 'yes_pose_detected'
                return

        if self.current_state == 'wait_for_current_pose':
            print('wait_for_current_pose')
            poses = eval(data.data)
            self.current_state = 'received_pose'
            self.current_param = poses


