from setuptools import find_packages, setup
import os 
from glob import glob

package_name = 'industrial_robot_arm'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*'))


    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mojtaba',
    maintainer_email='mojtaba@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "trajectory_msg = industrial_robot_arm.controller_test:main"
        ],
    },
)
