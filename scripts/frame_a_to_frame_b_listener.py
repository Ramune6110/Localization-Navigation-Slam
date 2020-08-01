import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('frame_a_frame_b_listener_node')
    listener = tf.TransformListener()
    rate = rospy.Rate(1.0)
    listener.waitForTransform('/frame_a', '/frame_b', rospy.Time(), rospy.Duration(2.0))

    while not rospy.is_shutdown():
        (translation,rotation) = listener.lookupTransform('/frame_a', '/frame_b', rospy.Time(0))
        rpy = tf.transformations.euler_from_quaternion(rotation)
        for i in range(3):
            print(translation[i])
            print(rpy[i])