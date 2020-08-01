#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <nav_msgs/Odometry.h>
#include <tf.h>
#include <math.h>

int main(int argc, char **argv)
{
    ros::init(argc, argv, "tf_convert");
    ros::NodeHandle nh;

    float roll  = math.radians(30);
    float pitch = math.radians(42);
    float yaw   = math.radians(58);

}
