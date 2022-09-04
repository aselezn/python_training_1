from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="new_name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="new_header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", footer="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(footer="new_footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)