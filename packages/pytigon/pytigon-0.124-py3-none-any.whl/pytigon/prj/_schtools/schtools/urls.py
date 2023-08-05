## -- coding: utf-8 --

from django.urls import path, re_path, include
from django.utils.translation import ugettext_lazy as _
from pytigon_lib.schviews import generic_table_start, gen_tab_action, gen_row_action
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    re_path("search/(?P<type>.+)/", views.autocomplete_search, {}),
    path("set_user_param/", views.set_user_param, {}),
    path("get_user_param/", views.get_user_param, {}),
    re_path(
        "(?P<app>[\w=_,;-]*)/(?P<table>[\w=_,;-]*)/import_table/$",
        views.import_table,
        {},
    ),
    path("form/ImportTableForm/", views.view_importtableform, {}),
]

gen = generic_table_start(urlpatterns, "schtools", views)


gen.standard("Parameter", _("Parameter"), _("Parameter"))
