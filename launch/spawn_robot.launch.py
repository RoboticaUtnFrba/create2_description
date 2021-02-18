#!/usr/bin/env python

# Copyright 2021 Emiliano Javier Borghi Orue.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Launch Webots iRobot Create 2 driver."""

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions.path_join_substitution import PathJoinSubstitution
from launch_ros.actions import Node


def generate_launch_description():
    package_dir = get_package_share_directory('create2_description')
    webots_core_dir = get_package_share_directory('webots_ros2_core')

    world = LaunchConfiguration('world')
    use_rviz = LaunchConfiguration('use_rviz')

    rviz_config = PathJoinSubstitution([package_dir, 'resource', 'bringup.rviz'])
    create_parameters = PathJoinSubstitution([package_dir, 'resource', 'irobot_create_2.yaml'])


    world_arg = DeclareLaunchArgument(
        'world',
        default_value='small_room.wbt',
        description='Choose one of the world files from `/create2_description/worlds` directory'
    )

    use_rviz_arg = DeclareLaunchArgument(
        'use_rviz',
        default_value='True',
        description='Whether to bringup RViz2 or not'
    )

    webots = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([webots_core_dir, 'launch', 'robot_launch.py'])
        ),
        launch_arguments={
            'package': 'create2_description',
            'executable': 'driver',
            'world': PathJoinSubstitution([package_dir, 'worlds', world]),
            'node_parameters': create_parameters,
            'robot_name': '',
            'use_sim_time': 'True',
            'publish_tf': 'True',
        }.items()
    )

    rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=['--display-config=' + rviz_config.perform(None)],
        condition=IfCondition(use_rviz)
    )

    return LaunchDescription([
        # Arguments
        world_arg,
        use_rviz_arg,
        # Nodes
        rviz2,
        webots,
    ])
