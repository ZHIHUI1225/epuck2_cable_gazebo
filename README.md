# environment:
ubuntu 20.04 + ros2 foxy + gazebo 11
workspace: Epuck2_ws
package: epuck2
# main folders:
## meshes:
the description of the epuck2
## worlds: 
empty world and world with walls
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
5. control the agents (namespace: agent1, agent2) with keyboard:
   ```
   ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r __ns:=/agent1
   ```
# adjuest tools:
1. urdf convert to sdf:
```
gz sdf -p /my_urdf.urdf > /my_sdf.sdf
```
2. sdf mode 路径设置：

(GAZEBO_MODEL_PATH is set in  .bashrc file)

models:// 被替换为GAZEBO_MODEL_PATH
file:// 被替换为GAZEBO_RESOURCE_PATH
参考链接： https://osrf-migration.github.io/sdformat-gh-pages/#!/osrf/sdformat/pull-requests/558/page/1
3. check urdf file 
```
check_urdf <(xacro model.urdf.xacro)
```

# problems still need to be solved:
## sdf model and urdf model
sdf can include other models by <include> </include>, but can not modify or add or remove models.(may be solved by update libsdformat, not sure weather works in ros foxy and gazebo11)

sdf cannot use the below params of epuck2:
```
<transmission name ="right_motor_t">
 <type>transmission_interface/SimpleTransmission</type>
 <joint name="right_joint">
  <hardwareInterface>EffortJointInterface</hardwareInterface>
 </joint>
 <actuator name="right_motor_m">
  <hardwareInterface>EffortJointInterface</hardwareInterface>
 <mechanicalReduction>50</mechanicalReduction>
 </actuator>
</transmission>
```
sdf can not define parameters to avoid repeated value changes.
In xacro, can use "<xacro:property name="lidar" value="true"/>"
### cable model
the damping, friction, and spring stiffness of joints need to be estimated properly.
### collision 
do not have collision detection.
### friction and mass balance of cable and agents.
# others
other deformable model tool: Isaac Gym, pybullet
