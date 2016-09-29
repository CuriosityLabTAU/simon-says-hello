class KinectPos():
    def __init__(self):
        self.poses_satisfied = [0,0,0]
        self.poses_names = ["right_hand_up","left_hand_up","two_hands_up"]
        self.poses_conditions = [""]
        self.positions = {'head':{}, 'neck':{}, 'torso':{}, 'left_shoulder':{}, 'left_elbow':{}, 'left_hand':{}, 'right_shoulder':{}, 'right_elbow':{}, 'right_hand':{}, 'left_hip':{}, 'left_knee':{}, 'left_foot':{}, 'right_hip':{}, 'right_knee':{}}





    def update_position(self,positions):
        names = ['head', 'neck', 'torso', 'left_shoulder', 'left_elbow', 'left_hand', 'right_shoulder', 'right_elbow', 'right_hand', 'left_hip', 'left_knee', 'left_foot', 'right_hip', 'right_knee', 'right_foot']

        for name in names:
            positions['head']['x'] = positions[names.index['head']].x



        left_hand_y = data.position[data.name.index('left_hand')].y
        right_hand_y = data.position[data.name.index('right_hand')].y
        left_shoulder_y = data.position[data.name.index('left_shoulder')].y
        right_shoulder_y = data.position[data.name.index('right_shoulder')].y
