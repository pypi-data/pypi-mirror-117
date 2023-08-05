## -- coding: utf-8 --

from django.urls import path, re_path, include
from django.utils.translation import ugettext_lazy as _
from pytigon_lib.schviews import generic_table_start, gen_tab_action, gen_row_action
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    re_path("grid/(?P<folder>.*)/(?P<value>[\w=]*)/$", views.grid, {}),
    re_path("open/(?P<file_name>.*)/$", views.open, {}),
    re_path("save/(?P<file_name>.*)/$", views.save, {}),
    re_path("open_page/(?P<file_name>.*)/(?P<page>\d+)/$", views.open_page, {}),
    path("form/FileManager/", views.view_filemanager, {}),
    path("form/Move/", views.view_move, {}),
    path("form/Copy/", views.view_copy, {}),
    path("form/MkDir/", views.view_mkdir, {}),
    path("form/Rename/", views.view_rename, {}),
    path("form/NewFile/", views.view_newfile, {}),
    path("form/Delete/", views.view_delete, {}),
    path("form/Setup/", views.view_setup, {}),
]

gen = generic_table_start(urlpatterns, "schcommander", views)
