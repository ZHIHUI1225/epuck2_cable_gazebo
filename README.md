# environment: ubuntu 20.04 + ros2 foxy + gazebo 11
workspace: Epuck2_ws
package: epuck2
# main folders:
meshes: the description of the epuck2
worlds: empty world and world with walls
## models: 
cable_test(cable model from changpang), urdf(ours)
### sdf models: 
Deformable_sysytem.sdf, includes cable, agent, agent1, agent2
### urdf model:
generate by .gazebo (plugin) and .urdf.xacro (geometry description)

## launch
multi robot launch: multi_box_bot_launch.py
sdf model launch: launch_sdf_into_gazebo.launch.py
urdf launch: world.launch.py , Epuckgazebo.launch.py

# use step
1. ```
   cd Epuck2_ws/
   ```
2.
   ```
    source install/setup.bash
   ```
3. ```
   colcon build
   ```
4.  ```
    ros2 launch epuck2 launch_sdf_into_gazebo.launch.py
     ```
    gazebo launch and model shows as follow:
      ![image](https://github.com/ZHIHUI1225/epuck2_cable_gazebo/assets/124249908/85d3d5b8-7ca8-4d48-8570-ccde7c17a45c)
5. control the agents with keyboard:
   '''
   ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r __ns:=/agent1
   '''

