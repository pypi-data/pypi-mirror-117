# -*- coding: utf-8 -*-

import django
from django.db import models

from pytigon_lib.schdjangoext.fields import *
from pytigon_lib.schdjangoext.models import *
import pytigon_lib.schdjangoext.fields as ext_models
from pytigon_lib.schtools import schjson

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

import os, os.path
import sys
from pytigon_lib.schhtml.htmltools import superstrip


from schsimplescripts.models import *

from schwiki.models import *

from schattachements.models import *

from schlog.models import *

from schtools.models import *

from schelements.models import *

from schreports.models import *

from schcommander.models import *

from schtasks.models import *


def get_projects():
    pass
