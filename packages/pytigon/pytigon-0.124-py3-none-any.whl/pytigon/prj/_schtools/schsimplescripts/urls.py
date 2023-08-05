## -- coding: utf-8 --

from django.urls import path, re_path, include
from django.utils.translation import ugettext_lazy as _
from pytigon_lib.schviews import generic_table_start, gen_tab_action, gen_row_action
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    gen_row_action("Scripts", "run", views.run),
    re_path("run/(?P<script_name>\w+)/$", views.run_script_by_name, {}),
    path("run_script/", views.run_script, {}),
]

gen = generic_table_start(urlpatterns, "schsimplescripts", views)


gen.standard("Scripts", _("Scripts"), _("Scripts"))
