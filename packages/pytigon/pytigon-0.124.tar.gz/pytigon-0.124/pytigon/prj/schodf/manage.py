#!/usr/bin/env python
import os
import sys
from os import environ

_lp = os.path.dirname(os.path.abspath(__file__))
os.chdir(_lp)
if not _lp in sys.path:
    sys.path.insert(0, _lp)
_rp2 = None

if "PYTIGON_ROOT_PATH" in environ:
    _rp = environ["PYTIGON_ROOT_PATH"]
    _rp2 = os.path.abspath(os.path.join(_rp, ".."))
else:
    _rp = os.path.abspath(os.path.join(_lp, "..", "..", ".."))

if not _rp in sys.path:
    sys.path.insert(0, _rp)
if _rp2 and not _rp2 in sys.path:
    sys.path.append(_rp2)

from pytigon_lib import init_paths

init_paths()

from pytigon_lib.schdjangoext.django_manage import *

if __name__ == "__main__":
    cmd(sys.argv, from_main=True)
