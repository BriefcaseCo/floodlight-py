from setuptools import setup, find_packages
from os import path

# Read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='floodlights',
    version='0.2',
    description='A CLI for controlling floodlight devices using the TinyTuya library.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/BriefcaseCo/floodlight-py',
    author='dddanmar',
    author_email='dddanmar@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='floodlights cli home automation',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,
    python_requires='>=3.6, <4',
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
