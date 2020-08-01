cmake_minimum_required(VERSION 3.0.2)
project(localization_navigation_slam)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  nav_msgs
  roscpp
  rospy
  std_msgs
  tf
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES localization_navigation_slam
#  CATKIN_DEPENDS geometry_msgs nav_msgs roscpp rospy std_msgs tf
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(frame_a_to_frame_b_broadcaster src/frame_a_to_frame_b_broadcaster.cpp)
target_link_libraries(frame_a_to_frame_b_broadcaster ${catkin_LIBRARIES})
