from setuptools import setup

package_name = 'agri_tracker'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='anesu',
    maintainer_email='anesu@todo.todo',
    description='Agri-Logistix IoT tracker simulation',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tracker_node = agri_tracker.tracker_node:main',
            'alert_node = agri_tracker.alert_node:main',
        ],
    },
)
