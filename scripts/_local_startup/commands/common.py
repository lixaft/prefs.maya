from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

from _local_startup.commands import export


@export("HelloWorld")
def hello_world():
    # type: () -> None
    """Prints "Hello World!" to the script editor."""
    sys.stdout.write("Hello World!\n")
