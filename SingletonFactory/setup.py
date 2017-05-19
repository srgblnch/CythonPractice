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

from setuptools import setup, find_packages, Command
try:
    from Cython.Build import cythonize
except ImportError:
    raise ImportError("Having Cython installed is required")
import os
# IMPORTANT: the setuptools import must be before the Cython one
#            if not, the cythonize() output will not be a:
#            <setuptools.extension.Extension object at 0x...> but a:
#            <distutils.extension.Extension object at 0x...>
#            that will not be accepted by the setup().


projectName = "barfoo"
shortDescription = "Python module to provide a Singleton Factory"
longDescription = """
This code is part of a Toy-project thought as a logbook of recipes for Cython
usage.
 
This part like to show how one can have a Factory object that is a singleton.
"""

classifiers = []
classifiers.append('Development Status :: 1 - Planning')
classifiers.append('Intended Audience :: Developers')
classifiers.append('License :: OSI Approved :: '
                   'GNU General Public License v3 or later (GPLv3+)')
classifiers.append('Operating System :: POSIX')
classifiers.append('Programming Language :: Cython')
classifiers.append('Topic :: Software Development :: Libraries :: '
                   'Python Modules')


def find_file_by_extension(path='.', ext='.pyx'):
    files = []
    for root, dirs, filenames in os.walk(path):
        for fname in filenames:
            if fname.endswith(ext):
                files.append(os.path.join(root, fname))
    return files

def find_directories(path='.', names=None):
    directories = []
    if names is not None and isinstance(names, list):
        for root, dirs, filenames in os.walk(path):
            if len(dirs) > 0 and dirs[0] in names:
                dname = "%s/%s" % (root, dirs[0])
                if not dname in directories:
                    directories.append(dname)
    return directories


def find_pyx(path='.'):
    return find_file_by_extension(path, ext='.pyx')


def find_so(path='.'):
    return find_file_by_extension(path, ext='.so')

# FIXME: it is call in all commands, even when 'clean'
def build_extension():
    """
        This method can be simply:
        return cythonize(find_pyx(), language_level=3)
        But, this way we will be able to add libraries and includes for each
        of the files if need be.
    """
    extensions = []
    files = find_pyx()
    for file in files:
        source = cythonize(file)
        extensions += source
    return extensions


class CleanCommand(Command):
    """Modify the clean command to remove the cythonized files."""
    user_options = []

    def initialize_options(self):
         pass

    def finalize_options(self):
        pass

    def run(self):
        sources = ['./build', './*.egg-info']
        files = []
        for fileName in find_pyx():
            files.append(fileName.replace('.pyx', '.c'))
        for soFile in find_so():
            files.append(soFile)
        for pyc in find_file_by_extension(ext='.pyc'):
            files.append(pyc)
        for file in files:
            os.system('rm -vrf %s' % file)
        for directory in find_directories(names=['__pycache__']):
            os.system('rm -vrf %s' % directory)

cmdclass = {}
cmdclass.update({'clean': CleanCommand})


setup(name=projectName,
      version=__version__,
      license=__license__,
      description=shortDescription,
      long_description=longDescription,
      author=__author__,
      author_email=__email__,
      setup_requires=['cython'],
      ext_modules=build_extension(),
      cmdclass=cmdclass,
      packages=find_packages(),
      classifiers=classifiers
      )
