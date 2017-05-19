# -*- coding: utf-8 -*-
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

__author__ = "Sergi Blanch-Torne"
__email__ = "srgblnchtrn@protonmail.ch"
__copyright__ = "Copyright 2017 Sergi Blanch-Torne"
__license__ = "GPLv3+"
__status__ = "development"
# we use semantic versioning (http://semver.org/) and we update it using the
# bumpversion script (https://github.com/peritus/bumpversion)
__version__ = '0.0.2-alpha'

from setuptools import setup, find_packages  #, Extension
try:
    from Cython.Build import cythonize
except ImportError:
    raise ImportError("Having Cython installed is required")
import os



projectName = "barfoo"
# shortDescription = "Python module to provide a Singleton Factory"
# longDescription = """
# This code is part of a Toy-project thought as a logbook of recipes for Cython
# usage.
# 
# This part like to show how one can have a Factory object that is a singleton.
# """

# classifiers = []
# classifiers.append('Development Status :: 1 - Planning')
# classifiers.append('Intended Audience :: Developers')
# classifiers.append('License :: OSI Approved :: '
#                    'GNU General Public License v3 or later (GPLv3+)')
# classifiers.append('Operating System :: POSIX')
# classifiers.append('Programming Language :: Cython')
# classifiers.append('Topic :: Software Development :: Libraries :: '
#                    'Python Modules')


def find_pyx(path='.'):
    pyx_files = []
    for root, dirs, filenames in os.walk(path):
        for fname in filenames:
            if fname.endswith('.pyx'):
                pyx_files.append(os.path.join(root, fname))
    print(pyx_files)
    return pyx_files


def build_extension():
    extensions = []
    files = find_pyx()
    for file in files:
        print(">> file: %s "% (file))
        source = cythonize(file)
        print(">> cythonized: %s" % (source[0].name))
        extensions.append(Extension(file,
                                    sources=cythonize(file)))
    # return cythonize(find_pyx(), language_level=3)
    return extensions


# class CleanCommand(Command):
#     """Modify the clean command to remove the cythonized files."""
#     user_options = []

#     def initialize_options(self):
#         pass

#     def finalize_options(self):
#         pass

#     def run(self):
#         sources = ['./build', './*.egg-info']
#         files = []
#         for fileName in find_pyx():
#             files.append(fileName.replace('.pyx', '.c'))
#         print(">> c files: %s" % files)
#         for soFile in find_so():
#             print(">> so file: %s" % fileName)
#             files.append(soFile)
#         for file in files:
#             os.system('rm -vrf %s' % file)

# cmdclass.update({'clean': CleanCommand})

sources = cythonize(find_pyx(), language_level=3)
print("%s = cythonize(%s)" % (sources, find_pyx()))


setup(name=projectName,
      version=__version__,
      #license=__license__,
      #description=shortDescription,
      #long_description=longDescription,
      #author=__author__,
      #author_email=__email__,
      #setup_requires=['cython'],
      ext_modules=cythonize(find_pyx(), language_level=3),
      #ext_modules=build_extension(),
      packages=find_packages(),
      #classifiers=classifiers
      )
