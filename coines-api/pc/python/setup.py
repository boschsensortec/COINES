#!/usr/bin/env python3

"""Python wrapper for coinesAPI

`coinespy` allows users to access the Bosch Sensortec Application Board using Python

- Control VDD and VDDIO of sensor
- Configure SPI and I2C bus parameters
- Read and write into registers of sensors from Bosch Sensortec via SPI and I2C
- Read and write digital pins of the Application Board.

"""
import shutil
import setuptools

DOCLINES = (__doc__ or '').split("\n")

shutil.copytree("../../../firmware", "firmware", dirs_exist_ok=True)
shutil.copytree("../../../tools", "tools", dirs_exist_ok=True)
setuptools.setup(
    name="coinespy",
    version="1.0.1",
    author="Bosch Sensortec GmbH",
    author_email="contact@bosch-sensortec.com",
    url="https://www.bosch-sensortec.com/",
    packages=['coinespy', 'firmware', 'tools'],
    package_data={'coinespy': ['libcoines_64.dll',
                               'libcoines_32.dll',
                               'libcoines_64.so',
                               'libcoines_32.so',
                               'libcoines_arm_64.dylib',
                               'libcoines_arm_32.dylib',
                               'libcoines_i386_64.dylib',
                               'libcoines_i386_32.dylib',
                               'libcoines_armv7_32.so',
                               'bin/*'],
                  'firmware': ['nicla/coines_bridge/*'
                               'app2.0/coines_bridge/*',
                               'app3.0/coines_bridge/*',
                               'firmware/app3.1/coines_bridge/*'],
                  'tools': ['usb-dfu/*', 'app20-flash/*.exe',
                            'app_switch/README.md', 'app_switch/*.exe',
                            'openocd/*']
                  },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X"
    ],
    python_requires='>=2.6, <4',
)
