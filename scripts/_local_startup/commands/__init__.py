from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pkgutil

from maya import cmds

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Callable
    from typing import TypeAlias

    Cmd = Callable[[], None]  # type: TypeAlias


def export(name, plugin=None):
    # type: (str, str | None) -> Callable[[Cmd], Cmd]
    def decorator(func):
        # type: (Cmd) -> Cmd
        if cmds.runTimeCommand(name, exists=True):
            cmds.runTimeCommand(name, edit=True, delete=True)

        cmd = "from {f.__module__} import {f.__name__}; {f.__name__}()"
        doc = func.__doc__ or ""
        cmds.runTimeCommand(
            name,
            command=cmd.format(f=func),
            commandLanguage="python",
            plugin=plugin,
            default=True,
            category="Lixaft",
            tags="lixaft",
            keywords="lixaft,starup,{}".format(func.__module__.split(".")[-1]),
            annotation=doc if not doc else doc.splitlines()[0],
            longAnnotation=doc,
        )

        return func

    return decorator


def load_all():
    # type: () -> None
    for _, name, _ in pkgutil.iter_modules(__path__):
        __import__(__name__ + "." + name)
