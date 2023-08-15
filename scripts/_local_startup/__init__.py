from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from maya import cmds

from _local_startup import commands
from _local_startup import hotkeys

ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
)


def setup():
    # type: () -> None
    commands.load_all()
    hotkeys.load_all()

    cmds.workspaceLayoutManager(
        i=os.path.join(ROOT, "workspaces", "Main.json"),
    )
