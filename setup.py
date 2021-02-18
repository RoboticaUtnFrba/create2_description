"""webots_ros2 package setup file."""

from glob import glob
import os
from setuptools import setup

package_name = 'create2_description'

data_files = []
# Install marker file in the package index
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
# Include our package.xml file`
data_files.append(('share/' + package_name, ['package.xml']))
# Include all launch files
data_files.append((os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')))
# World files
data_files.append((os.path.join('share', package_name, 'worlds'), glob('worlds/*.wb*')))
data_files.append((os.path.join('share', package_name, 'worlds/textures'), glob('worlds/textures/*')))
# Configuration files
data_files.append(('share/' + package_name + '/resource', [
    'resource/irobot_create_2.yaml',
    'resource/bringup.rviz',
]))
# Proto
data_files.append((os.path.join('share', package_name, 'protos'), glob('protos/*.proto')))
data_files.append((os.path.join('share', package_name, 'protos/textures'), glob('protos/textures/*.jpg')))

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    author='Emiliano J. Borghi Orue',
    author_email='eborghiorue@frba.utn.edu.ar',
    maintainer='Emiliano J. Borghi Orue',
    maintainer_email='eborghiorue@frba.utn.edu.ar',
    keywords=['ROS', 'Webots', 'Robot', 'Simulation', 'iRobot Create 2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='iRobot Create 2 ROS2 interface.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'driver = create2_description.driver:main'
        ],
        'launch.frontend.launch_extension': ['launch_ros = launch_ros']
    }
)
