import sys
import os

from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, TextSubstitution
import launch.actions
import launch_ros.actions

def gen_robot_list(number_of_robots):

    robots = []

    for i in range(number_of_robots):
        robot_name = "box_bot"+str(i)
        x_pos = float(i)
        robots.append({'name': robot_name, 'x_pose': x_pos, 'y_pose': 0.0, 'z_pose': 0.01})


    return robots 

def generate_launch_description():

    return LaunchDescription([
        launch_ros.actions.Node(
            package='epuck2',
            executable='spawn_box_bot_v2.py',
            output='screen',
            arguments=[
                '--robot_urdf', launch.substitutions.LaunchConfiguration('robot_urdf'),
                '--robot_name', launch.substitutions.LaunchConfiguration('robot_name'),
                '--robot_namespace', launch.substitutions.LaunchConfiguration('robot_namespace'),
                '-x', launch.substitutions.LaunchConfiguration('x'),
                '-y', launch.substitutions.LaunchConfiguration('y'),
                '-z', launch.substitutions.LaunchConfiguration('z')]),
    ])


def generate_launch_description():

    robot_name = 'epuck2'
    urdf = os.path.join(get_package_share_directory('box_bot_description'), 'robot/', 'box_bot_v2.urdf')
    urdf = os.path.join(get_package_share_directory(robot_name), 'models/urdf', 'Epuck2.urdf')
    pkg_box_bot_description = get_package_share_directory('box_bot_description')
    assert os.path.exists(urdf), "Thebox_bot.urdf doesnt exist in "+str(urdf)

    # Names and poses of the robots
    robots = gen_robot_list(3)

    # We create the list of spawn robots commands
    spawn_robots_cmds = []
    for robot in robots:
        spawn_robots_cmds.append(
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(os.path.join(pkg_box_bot_description, 'launch',
                                                           'spawn_box_bot_launch.py')),
                launch_arguments={
                                  'robot_urdf': urdf,
                                  'x': TextSubstitution(text=str(robot['x_pose'])),
                                  'y': TextSubstitution(text=str(robot['y_pose'])),
                                  'z': TextSubstitution(text=str(robot['z_pose'])),
                                  'robot_name': robot['name'],
                                  'robot_namespace': robot['name']
                                  }.items()))

    # Create the launch description and populate
    ld = LaunchDescription()
    
    for spawn_robot_cmd in spawn_robots_cmds:
        ld.add_action(spawn_robot_cmd)

    return ld