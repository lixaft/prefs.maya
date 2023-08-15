from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from maya import cmds

SET = "lixaft"


def _create(keymap, command):
    # type: (str, str) -> None
    keys = keymap.lower().split("+")
    cmds.hotkey(
        name=cmds.nameCommand(
            command + "NC",
            annotation=command,
            command=command,
            default=True,
        ),
        altModifier="alt" in keys,
        ctrlModifier="ctrl" in keys,
        shiftModifier="shift" in keys,
        keyShortcut=keys[-1],
    )


def load_all():
    # type: () -> None
    if cmds.hotkeySet(SET, exists=True):
        cmds.hotkeySet(SET, edit=True, delete=True)
    cmds.hotkeySet(SET, current=True, source="Maya_Default")

    _create("Ctrl+Shift+h", "HelloWorld")

    # Manipulation tools.
    _create("u", "MoveTool")
    _create("e", "RotateTool")
    _create("o", "ScaleTool")
    _create("a", "SelectTool")
