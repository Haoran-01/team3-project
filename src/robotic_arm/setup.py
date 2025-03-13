from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'robotic_arm'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sfr2024',
    maintainer_email='haoran.yan01@gmail.com',
    description='Robotic arm control package for pick-and-place tasks',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
    		'px100_pick_and_place = robotic_arm.px100_pick_and_place:main'
        ],
    },
)
