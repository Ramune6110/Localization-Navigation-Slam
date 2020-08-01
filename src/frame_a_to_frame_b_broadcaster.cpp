#include <ros/ros.h>
#include <tf/transform_broadcaster.h>

int main(int argc, char** argv)
{
    ros::init(argc, argv, "frame_a_to_frame_b_broadcaster");
    ros::NodeHandle node;

    tf::TransformBroadcaster br;
    tf::Transform transform;

    ros::Rate rate(2.0);

    float x  = 1.0;
    float y  = 2.0;
    float z  = 3.0;
    float qx = 0.0;
    float qy = 0.0;
    float qz = 0.0;
    float qw = 1.0;
    
    while (ros::ok()) {
        transform.setOrigin(tf::Vector3(x, y, z));
        transform.setRotation(tf::Quaternion(qx, qy, qz, qw));
        br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "frame_b", "frame_a"));
        rate.sleep();
    }

    return 0;
}