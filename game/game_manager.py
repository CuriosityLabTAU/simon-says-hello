from interaction_control.component import *
import rospy
#import String


class GameManager(Component):
    #kinect_listener = None

    def start(self):
        print('Starting GameManager')
        self.current_state = 'started'

        rospy.init_node('kinect_listener', anonymous=True)
        rospy.Subscriber("skeleton", skeleton, self.got_pose)
        rospy.spin()
