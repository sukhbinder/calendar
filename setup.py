import os
from setuptools import find_packages, setup

setup(
    name="cal",
    version="1.0",
    packages=find_packages(),
    license="Private",
    description="cal in cmd",
    author="sukhbinder",
    author_email="sukh2010@yahoo.com",
    entry_points={
        'console_scripts': ['cal = showCalendar:main',],
    }
)
