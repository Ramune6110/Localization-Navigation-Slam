import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
import tf

#Eulerian Angle to Quaternion Conversion
roll  = math.radians(30)
pitch = math.radians(42)
yaw   = math.radians(58)
quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw)

for i in range(4):
    print(quaternion[i])

#Quaternion to Eulerian Angle Conversion
rpy = tf.transformations.euler_from_quaternion(quaternion)
roll_from_quaternion  = rpy[0]
pitch_from_quaternion = rpy[1]
yaw_from_quaternion   = rpy[2]

for i in range(3):
    print(rpy[i])

#Convert the appropriate quaternion to Eulerian angle
q = (-3.88256895463e-06, 0.0015896463485, 0.001397167245, 0.0)
rpy = tf.transformations.euler_from_quaternion(q)
roll_from_quaternion  = rpy[0]
pitch_from_quaternion = rpy[1]
yaw_from_quaternion   = rpy[2]

for i in range(3):
    print(rpy[i])


