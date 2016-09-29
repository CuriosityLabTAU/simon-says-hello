import rospy
from skeleton_markers.msg import Skeleton
from kinect_pos import KinectPose



def callback(data):
    # get the data (name, position)
    kid_pose = KinectPose()
    kid_pose.update_position(data.position)

def kinect_listener():
    #init a listener to kinect and
    rospy.init_node('kinect_listener', anonymous=True)
    rospy.Subscriber("skeleton", Skeleton, callback)
    rospy.spin()


l = kinect_listener()
