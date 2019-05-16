# -*- coding: utf-8 -*-
u"""
Copyright 2019 Alvaro Lopez-Gil Navajas - ElevenPaths, Telefonica
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from distutils.core import setup

setup(
    name='masappcli',
    packages=['masappci'],
    version='0.1',
    license='MIT',
    description='',
    author='alopezna5',
    url='https://github.com/alopezna5/mASAPP_CI',
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz', #TODO
    keywords=['MOBILE', 'ANDROID', 'IOS', 'CONTINUOUS INTEGRATION'],
    install_requires=[  #TODO
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
    entry_points={
        'console_scripts': [
            'masappcli = masappci.__main__:main',
        ]
    }
)
