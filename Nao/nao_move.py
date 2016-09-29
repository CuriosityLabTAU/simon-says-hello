# -*- encoding: UTF-8 -*-

''' PoseInit: Small example to make Nao go to an initial position. '''

import sys
import almath
from naoqi import ALProxy
import rospy


class NaoNode:

    def __init__(self):
        robotIP = '192.168.0.100'
        port = 9559

        try:
            self.motionProxy = ALProxy("ALMotion", robotIP, port)
        except Exception,e:
            print "Could not create proxy to ALMotion"
            print "Error was: ",e
            sys.exit(1)

        # Get the Robot Configuration
        self.robotConfig = self.motionProxy.getRobotConfig()

    def move_to_pose(self, pose):
        Head     = [pose['HeadYawAngle'], pose['HeadPitchAngle']]

        LeftArm  = [pose['ShoulderPitchAngle'], +pose['ShoulderRollAngle'],
                    +pose['ElbowYawAngle'], +pose['ElbowRollAngle'], pose['WristYawAngle'], pose['HandAngle']]
        RightArm = [pose['ShoulderPitchAngle'], -pose['ShoulderRollAngle'], -pose['ElbowYawAngle'], -pose['ElbowRollAngle'], pose['WristYawAngle'], pose['HandAngle']]

        LeftLeg  = [0.0,                      #hipYawPitch
                    pose['spreadAngle'],              #hipRoll
                    -pose['kneeAngle']/2-pose['torsoAngle'],  #hipPitch
                    pose['kneeAngle'],                #kneePitch
                    -pose['kneeAngle']/2,             #anklePitch
                    -pose['spreadAngle']]             #ankleRoll
        RightLeg = [0.0, -pose['spreadAngle'], -pose['kneeAngle']/2-pose['torsoAngle'], pose['kneeAngle'], -pose['kneeAngle']/2,  pose['spreadAngle']]

        # Gather the joints together
        pTargetAngles = Head + LeftArm + LeftLeg + RightLeg + RightArm

        # Convert to radians
        pTargetAngles = [ x * almath.TO_RAD for x in pTargetAngles]

        #------------------------------ send stiffness -----------------------------
        self.motionProxy.stiffnessInterpolation("Body", 1.0, 0.5)

        #------------------------------ send the commands -----------------------------
        # We use the "Body" name to signify the collection of all joints
        pNames = "Body"
        # We set the fraction of max speed
        pMaxSpeedFraction = 0.2
        # Ask motion to do this with a blocking call
        self.motionProxy.angleInterpolationWithSpeed(pNames, pTargetAngles, pMaxSpeedFraction)


pose = {
    'HeadYawAngle'       : - 20.0,
    'HeadPitchAngle'     : + 0.0,

    'ShoulderPitchAngle' : +50.0,
    'ShoulderRollAngle'  : +50.0,
    'ElbowYawAngle'      : -50.0,
    'ElbowRollAngle'     : -50.0,
    'WristYawAngle'      : + 0.0,
    'HandAngle'          : + 0.0,

    # Define legs position
    'kneeAngle'    : +40.0,
    'torsoAngle'   : + 0.0, # bend the torso
    'spreadAngle'  : + 0.0 # spread the legs
}

try:
    nao = NaoNode()
    nao.move_to_pose(pose)
except rospy.ROSInterruptException:
    pass


