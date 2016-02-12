from distutils.core import setup
import sys

import bcloud_core

if sys.version_info.major < 3:
    raise Exception('Python 3 required')

setup(
    name='bcloud_core',
    version=bcloud_core.__version__,
    description='A fork of bcloud',
    long_description=open('README.rst').read(),

    license='GPLv3',
    url='https://github.com/stepheny/bcloud-core',
    author='LiuLang',
    author_email='gsushzhsosgsu@gmail.com',

    packages=['bcloud_core'],

    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )
