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
__email__ = "sblanch@cells.es"
__copyright__ = "Copyright 2017 Sergi Blanch-Torne"
__license__ = "GPLv3+"
__status__ = "development"

# Look at https://en.wikipedia.org/wiki/Software_versioning

# we use semantic versioning (http://semver.org/) and we update it using the
# bumpversion script (https://github.com/peritus/bumpversion)

__version__ = '0.0.2-alpha'


def version():
    return __version__


def versiontuple():
    if '-' in __version:
        _v, _rel = __version__.split('-')
    else:
        _v, _rel = __version__, ''
    _v = [int(n) for n in _v.split('.')]
    if len(_rel) > 0:
        _v += [_rel]
    return tuple(_v)

