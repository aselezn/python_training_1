from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first_group(Group(name="name_edited", header="header_edited", footer="footer_edited"))
    app.session.logout()