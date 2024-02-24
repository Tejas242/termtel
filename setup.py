from setuptools import setup
setup(
    name = 'termtel',
    version = '0.1.0',
    packages = ['termtel'],
    entry_points = {
        'console_scripts': [
            'termtel = termtel.__main__:main'
        ]
    })