# Copyright 2019 Open Source Robotics Foundation, Inc.
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

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    pkg_ros_gz_sim_demos = get_package_share_directory('ros_gz_sim_demos')

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'ros_gz_sim.launch.py')),
        launch_arguments={
            'world_sdf_file': 'sensors.sdf',
            'config_file': os.path.join(pkg_ros_gz_sim_demos,
                                        'config', 'imu.yaml'),
        }.items(),
    )

    return LaunchDescription([
        gz_sim,
        DeclareLaunchArgument(
            'rviz', default_value='true', description='Open RViz.'
        ),
        # rviz
    ])
