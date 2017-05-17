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
__version__ = '0.0.2'

try:
    from Cython.Build import cythonize
    from Cython.Distutils import build_ext
except ImportError:
    use_cython = False
else:
    use_cython = True
from os import system
from setuptools import setup, Extension, Command


projectName = "Factory"
shortDescription = "Python module to provide a Singleton Factory"
longDescription = """
This code is part of a Toy-project thought as a logbook of recipes for Cython
usage.

This part like to show how one can have a Factory object that is a singleton.
"""

extensions = [{'name': projectName,
               'dir': 'Factory',
               'src': ['__init__.pyx']}]

packages = [extensions[i]['name'] for i in range(len(extensions))]
ext_modules = []
for extension in extensions:
    files = []
    for fileName in extension['src']:
        files.append("%s/%s" % (extension['dir'], fileName))
    if use_cython:
        source = cythonize(files)
    else:
        source = [fileName.replace('.pyx', '.c') for fileName in files]
    ext_modules += [Extension(extension['name'], files)]

cmdclass = {'build_ext': build_ext}

classifiers = []
classifiers.append('Development Status :: 1 - Planning')
classifiers.append('Intended Audience :: Developers')
classifiers.append('License :: OSI Approved :: '
                   'GNU General Public License v3 or later (GPLv3+)')
classifiers.append('Operating System :: POSIX')
classifiers.append('Programming Language :: Cython')
classifiers.append('Topic :: Software Development :: Libraries :: '
                   'Python Modules')


class CleanCommand(Command):
    """Modify the clean command to remove the cythonized files."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        sources = ['./build', './*.egg-info']
        for extension in extensions:
            sources += ["./%s/%s" % (extension['dir'],
                                     file.replace('.pyx', '.c'))
                        for file in extension['src']]
        for file in sources:
            system('rm -vrf %s' % file)

cmdclass.update({'clean': CleanCommand})


configuration = {'name': projectName,
                 'version': __version__,
                 'license': __license__,
                 'description': shortDescription,
                 'long_description': longDescription,
                 'author': __author__,
                 'author_email': __email__,
                 'setup_requires': ['cython'],
                 'ext_modules': ext_modules,
                 'cmdclass': cmdclass,
                 'packages': packages,
                 'classifiers': classifiers}


setup(**configuration)
