import json

class KinectPose():
    def __init__(self):
        self.poses_satisfied = []
        self.poses_names = []
        self.poses_conditions = []
        self.positions = {'head':{}, 'neck':{}, 'torso':{}, 'left_shoulder':{}, 'left_elbow':{}, 'left_hand':{}, 'right_shoulder':{}, 'right_elbow':{}, 'right_hand':{}, 'left_hip':{}, 'left_knee':{}, 'left_foot':{}, 'right_hip':{},
                          'right_knee':{},'right_foot':{}}
        with open("poses_logics.json") as data_file:
            logics_json = json.load(data_file)
            self.poses_conditions = logics_json['conditions']
            self.poses_names = logics_json['names']
            print(self.poses_conditions,self.poses_names)


    def update_position(self,positions):
        names = ['head', 'neck', 'torso', 'left_shoulder', 'left_elbow', 'left_hand', 'right_shoulder', 'right_elbow', 'right_hand', 'left_hip', 'left_knee', 'left_foot', 'right_hip', 'right_knee', 'right_foot']
        for name in names:
            self.positions[name]['x'] = positions[names.index(name)].x
            self.positions[name]['y'] = positions[names.index(name)].y
            self.positions[name]['z'] = positions[names.index(name)].z

        print (self.positions['head']['x'])

    def parse_condition(self):
        print("r")

   #def check_condition
