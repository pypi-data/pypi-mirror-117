# -*- coding: utf-8 -*-
from setuptools import setup

setup(
  name="save-text",
  version="1.0.0",
  description='You can save and retrieve text.',
  author='YahiroRyo',  
  author_email='YahiroRyo@users.noreply.github.com',
  url="https://github.com/YahiroRyo",
  license='MIT',
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  entry_points={
    "console_scripts":[
      "save-text = save:main"
    ]
  }
)