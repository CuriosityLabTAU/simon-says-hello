import rospy
from skeleton_markers.msg import Skeleton
from kinect_pos import KinectPose



def callback(data):
    # get the data (name, position)

    left_hand_y = data.position[data.name.index('left_hand')].y
    right_hand_y = data.position[data.name.index('right_hand')].y
    left_shoulder_y = data.position[data.name.index('left_shoulder')].y
    right_shoulder_y = data.position[data.name.index('right_shoulder')].y

    print(data.position[data.name.index('right_hand')].x, data.position[data.name.index('right_hand')].y)
    # output gestures
    if right_hand_y > right_shoulder_y and left_hand_y > left_shoulder_y:
        print('both hands up')
    elif right_hand_y > right_shoulder_y:
        print('right hand up')
    elif left_hand_y > left_shoulder_y:
        print('left hand up"')
    elif right_hand_y > right_shoulder_y and left_hand_y > left_shoulder_y:
        print('both hands up')
    else:
        print('no')
    #
    #
    #

    pose = KinectPose()
    pose.update_position(data.position)

    # print(data.position)
#['head', 'neck', 'torso', 'left_shoulder', 'left_elbow', 'left_hand', 'right_shoulder', 'right_elbow', 'right_hand', 'left_hip', 'left_knee', 'left_foot', 'right_hip', 'right_knee', 'right_foot']

def kinect_listener():
    rospy.init_node('kinect_listener', anonymous=True)
    rospy.Subscriber("skeleton", Skeleton, callback)
    rospy.spin()

l = kinect_listener()
