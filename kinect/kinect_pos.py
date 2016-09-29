class KinectPose():
    def __init__(self):
        self.poses_satisfied = [0,0,0]
        self.poses_names = ["right_hand_up","left_hand_up","two_hands_up"]
        self.poses_conditions = [""]
        self.positions = {'head':{}, 'neck':{}, 'torso':{}, 'left_shoulder':{}, 'left_elbow':{}, 'left_hand':{}, 'right_shoulder':{}, 'right_elbow':{}, 'right_hand':{}, 'left_hip':{}, 'left_knee':{}, 'left_foot':{}, 'right_hip':{},
                          'right_knee':{},'right_foot':{}}



    def update_position(self,positions):
        names = ['head', 'neck', 'torso', 'left_shoulder', 'left_elbow', 'left_hand', 'right_shoulder', 'right_elbow', 'right_hand', 'left_hip', 'left_knee', 'left_foot', 'right_hip', 'right_knee', 'right_foot']
        for name in names:
            self.positions[name]['x'] = positions[names.index(name)].x
            self.positions[name]['y'] = positions[names.index(name)].y
            self.positions[name]['z'] = positions[names.index(name)].z

        print (self.positions['head']['x'])
