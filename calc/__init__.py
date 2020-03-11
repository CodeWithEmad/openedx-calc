"""
Ideally, we wouldn't need to pull in all the calc symbols here,
but courses were using 'import calc', so we need this for
backwards compatibility
"""
from __future__ import absolute_import
from .calc import *

__version__ = '1.0.2'  # pragma: no cover
