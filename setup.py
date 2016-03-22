#!/usr/bin/env python

import os
import distutils.extension
import distutils.command.build_ext

from setuptools import setup

class riak_pb_build_ext(distutils.command.build_ext.build_ext):
    def build_extensions(self):
        for e in self.extensions:
            # e.extra_compile_args = [ '-v' ]
            if e.name == 'riak._riak_kv_pbcpp':
                # NB: can add '-v' to args
                ld_path_arg = '-L{}'.format(os.path.dirname(self.get_ext_fullpath(e.name)))
                e.extra_link_args = [ ld_path_arg, '-l:_riak_pbcpp.so']
        distutils.command.build_ext.build_ext.build_extensions(self)

setup(
    name='riak-python-pbcpp',
    version='0.0.1',
    packages=[ 'riak' ],
    description='Test Python + CPP',
    ext_modules=[
        distutils.extension.Extension('riak._riak_pbcpp',
            sources=['src/_riak_pbcpp.cc','src/riak.pb.cc'],
            libraries=['protobuf']),
        distutils.extension.Extension('riak._riak_kv_pbcpp',
            sources=['src/_riak_kv_pbcpp.cc','src/riak_kv.pb.cc'],
            libraries=['protobuf'])
    ],
    license='Public Domain',
    platforms='Platform Independent',
    author='Luke Bakken',
    author_email='luke@bakken.io',
    url='https://github.com/lukebakken/riak-python-pbcpp',
    cmdclass={
        'build_ext': riak_pb_build_ext
    },
    classifiers=['License :: OSI Approved :: Public Domain License',
                 'Intended Audience :: Developers',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Topic :: Database']
)
