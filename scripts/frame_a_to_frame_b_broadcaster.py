import roslib
import rospy
import tf
import time  
import math
import time

if __name__ == '__main__':
    #child frame, parent frame
    rospy.init_node("frame_a_frame_b_broadcaster_node", anonymous=True)
    time.sleep(2)
    transform_broadcaster = tf.TransformBroadcaster()

    while not rospy.is_shutdown():
        roll  = 0.2
        pitch = 0.3
        yaw   = 0.1
        #Rotation
        rotation_quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
        #Translation
        x = 1.0
        y = 2.0
        z = 3.0
        translation_vector = (x, y, z)
        #time
        current_time = rospy.Time.now()
        #child frame:frame b, parent frame:frame a
        transform_broadcaster.sendTransform(
            translation_vector, 
            rotation_quaternion,
            current_time, 
            "frame_b", "frame_a" 
        )
        time.sleep(0.5)
        
    rospy.spin()