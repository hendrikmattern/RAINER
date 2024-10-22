#!/usr/bin/env python

from distutils.core import setup

setup(name='rainer',
      version='0.0.1',
      description='Resting stAte tIme and frequeNcy analyzER (RAINER)',
      author='Hendrik Mattern',
      #author_email='gward@python.net',
      #url='https://www.python.org/sigs/distutils-sig/',
      packages=['distutils', 'distutils.command', 'scipy', 'nibabel', 'matplotlib'],
      )
