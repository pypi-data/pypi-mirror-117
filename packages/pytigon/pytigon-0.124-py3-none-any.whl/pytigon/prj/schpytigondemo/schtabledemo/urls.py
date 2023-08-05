## -- coding: utf-8 --

from django.urls import path, re_path, include
from django.utils.translation import ugettext_lazy as _
from pytigon_lib.schviews import generic_table_start, gen_tab_action, gen_row_action
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path(
        "tbl_grid", TemplateView.as_view(template_name="schtabledemo/tbl_grid.html"), {}
    ),
]

gen = generic_table_start(urlpatterns, "schtabledemo", views)


gen.standard("demo_tbl", _("Grid table"), _("Grid table"))
