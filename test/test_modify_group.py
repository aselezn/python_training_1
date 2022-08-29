from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="new_name"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test"))
    app.group.modify_first_group(Group(header="new_header"))


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", footer="test"))
    app.group.modify_first_group(Group(footer="new_footer"))