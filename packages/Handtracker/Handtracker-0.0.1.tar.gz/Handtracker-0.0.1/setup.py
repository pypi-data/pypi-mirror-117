from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Soura'
LONG_DESCRIPTION = 'It is package or module used to trackhands. It can track the hands very easily and perfect for beginners. With this you can creat awesome projects. It uses open Cv2 to do the process.'

# Setting up
setup(
    name="Handtracker",
    version=VERSION,
    author="Soura Kanti Haldar",
    author_email="sourakantihaldar8@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['time' , 'cv2' , 'mediapipe'],
    keywords=['arithmetic', 'math', 'mathematics', 'python tutorial', 'avi upadhyay' , 'soura kanti' , 'opencv2' , 'handtracking', 'mediapipe','cv2','python','soura','package','module','numpy','hand tracker','soura','halder'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",])