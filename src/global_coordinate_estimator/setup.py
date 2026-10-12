from setuptools import setup

package_name = 'global_coordinate_estimator'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='student@example.com',
    description='Global coordinate estimation node for a differential-drive mobile robot.',
    license='Apache-2.0',
    entry_points={'console_scripts': [
        'global_coordinate_estimation = global_coordinate_estimator.global_coordinate_estimation:main',
	'odom_to_global = global_coordinate_estimator.odom_to_global:main',
    ]},
)
