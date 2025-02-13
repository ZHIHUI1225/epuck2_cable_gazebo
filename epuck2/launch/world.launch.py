import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

# this is the function launch  system will look for

def generate_launch_description():

    robot_name = 'epuck2'
    world_file_name = 'new.world'

    # full  path to urdf and world file
    
    world = os.path.join(get_package_share_directory(robot_name), 'worlds', world_file_name)

    urdf = os.path.join(get_package_share_directory(robot_name), 'models/urdf', 'bocbot.urdf')
    
    cable=os.path.join(get_package_share_directory(robot_name), 'models/cable_test', 'model.sdf')
    # read urdf contents because to spawn an entity in 
    # gazebo we need to provide entire urdf as string on  command line

    xml = open(urdf, 'r').read()
    cable_xml=open(cable,'r').read()
    # double quotes need to be with escape sequence
    xml = xml.replace('"', '\\"')
    cable_xml=cable_xml.replace('"','\\"')
    # this is argument format for spwan_entity service 
    spwan_args = '{name: \"bocbot\", xml: \"'  +  xml + '\" }'
    cable_args='{name: \"cable\", xml: \"'+cable_xml+'\" }'
    # create and return launch description object
    return LaunchDescription([

        # start gazebo, notice we are using libgazebo_ros_factory.so instead of libgazebo_ros_init.so
        # That is because only libgazebo_ros_factory.so contains the service call to /spawn_entity
        ExecuteProcess(
            cmd=['gazebo', '--verbose', world, '-s', 'libgazebo_ros_factory.so'],
            output='screen'),

        # tell gazebo to spwan your robot in the world by calling service
        ExecuteProcess(
            cmd=['ros2', 'service', 'call', '/spawn_entity', 'gazebo_msgs/SpawnEntity', spwan_args],
            output='screen'),

        ExecuteProcess(
            cmd=['ros2', 'service', 'call', '/spawn_entity', 'gazebo_msgs/SpawnEntity', cable_args],
            output='screen'),
    ])
