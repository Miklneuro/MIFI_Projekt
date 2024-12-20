from setuptools import setup, find_packages
import codecs

setup(
    name="zaryadye_bot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy',
        'tensorflow',
        'python-telegram-bot',
        'Pillow'
    ],
    author="Miklneuro",
    description="Bot for plant recognition",
    long_description=codecs.open("README.md", "r", "utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Miklneuro/MIFI_Projekt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
