import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
import time
from std_srvs.srv import Empty
import tf

def odomPoseCallback(odom_msg):
    print('x = ', odom_msg.pose.pose.position.x)
    print('y = ', odom_msg.pose.pose.position.y)
    #get the velocity of the robot
    print('vx = ', odom_msg.twist.twist.linear.x)
    print('vz = ', odom_msg.twist.twist.angular.z)
    #print the values of the orientation in quaternion
    print('qx=', odom_msg.pose.pose.orientation.x)
    print('qy=', odom_msg.pose.pose.orientation.y)
    print('qz=', odom_msg.pose.pose.orientation.z)
    print('qw=', odom_msg.pose.pose.orientation.w)

    quaternion = (
        odom_msg.pose.pose.orientation.x, 
        odom_msg.pose.pose.orientation.y,
        odom_msg.pose.pose.orientation.z,
        odom_msg.pose.pose.orientation.w
    )

    rpy   = tf.transformations.euler_from_quaternion(quaternion)
    roll  = rpy[0]
    pitch = rpy[1]
    yaw   = rpy[2]

    for i in range(3):
        print(rpy[i])

if __name__ == '__main__':
    rospy.init_node('turtlebot3_motion_pose', anonymous=True)
    pose_subscriber = rospy.Subscriber("/odom", Odometry, odomPoseCallback) 
    rospy.spin()