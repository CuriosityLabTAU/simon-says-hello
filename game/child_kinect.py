from interaction_control.component import *
import rospy
#import String


class ChildKinect(Component):
    kinect_listener = None

    def start(self):
        print('Starting kinect')
        self.current_state = 'started'

        rospy.init_node('kinect_listener', anonymous=True)
        rospy.Subscriber("skeleton", skeleton, self.got_pose)
        rospy.spin()

    def wait_for_start_pose(self):
        self.current_state = 'wait_for_start_pose'

    def wait_for_yes_pose(self):
        self.current_state = 'wait_for_yes_pose'

    def got_pose(self, data):
        poses = eval(data.data)

        if self.current_state == 'wait_for_start_pose':
            print('check if poses is only start pose')
            poses = eval(data.data)
            self.current_state = "start_pose_detected"
            return

        if self.current_state == 'wait_for_yes_pose':
            print('check if poses is only yes pose')
            poses = eval(data.data)
            self.current_state = "yes_pose_detected"
            return
