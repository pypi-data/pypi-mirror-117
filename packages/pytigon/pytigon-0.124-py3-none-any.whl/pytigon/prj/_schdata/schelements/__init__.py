from django.utils.translation import ugettext_lazy as _

ModuleTitle = _("main tools")
Title = _("Elements")
Perms = False
Index = ""
Urls = (
    ("table/Element/0/form/tree/?schtml=desktop", _("Elements"), None, """bi-stack"""),
    (
        "table/DocReg/-/form/list/?schtml=desktop",
        _("Documents register"),
        None,
        """client://actions/folder-new.png""",
    ),
    (
        "table/DocType/-/form/list/?schtml=desktop",
        _("Types of documents"),
        None,
        """""",
    ),
    (
        "table/DocRegStatus/-/form/list/?schtml=desktop",
        _("Definition of document status"),
        None,
        """ART_INFORMATION""",
    ),
    (
        "table/Account/0/form/tree/?schtml=desktop",
        _("Accounts"),
        None,
        """client://apps/system-file-manager.png""",
    ),
    (
        "table/AccountState/-/form/list/?schtml=desktop",
        _("States of accounts"),
        None,
        """client://mimetypes/package-x-generic.png""",
    ),
    (
        "table/AccountOperation/-/form/list/?schtml=desktop",
        _("Account operations"),
        None,
        """client://actions/edit-find-replace.png""",
    ),
    (
        "table/DocHead/-/form/list/?schtml=desktop",
        _("Documents"),
        None,
        """client://actions/format-justify-fill.png""",
    ),
    (
        "table/DocHead/rep_safety/form/docheadlist/?schtml=desktop",
        _("Documents [safety]"),
        None,
        """client://categories/applications-development.png""",
    ),
    (
        "table/DocHead/admin_delegation/form/docheadlist/?schtml=desktop",
        _("DEL"),
        None,
        """client://actions/mail-send-receive.png""",
    ),
)
UserParam = {}
