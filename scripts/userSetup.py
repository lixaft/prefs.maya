"""User setup for Maya.

This file is executed when Maya starts up.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from pprint import pprint

import _local_startup
from maya import cmds
from maya import mel

pp = pprint

cmds.evalDeferred(_local_startup.setup)
