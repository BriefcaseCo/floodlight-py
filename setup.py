from setuptools import setup, find_packages

setup(
    name='floodlights',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'tinytuya',
        'click',
        'configparser'
    ],
    entry_points='''
        [console_scripts]
        floodlights=floodlights:cli
    ''',
)
