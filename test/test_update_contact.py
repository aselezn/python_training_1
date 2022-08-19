from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.update_contact(Contact (name="name_updated", middlename="middlename_updated", lastname="lastname_updated", nickname="nickname_updated", title="title_updated", company="company_updated", address_1="address, 1 updated",
                                            phone_home="5555511", mobile_home="2222211", phone_work="3333311", fax="4444411", email_1="email_1_updated@mail.ru", email_2="email_2_updated@mail.ru", email_3="email_3_updated@mail.ru",
                                            homepage="homepage_updated", bday= "2", bmonth="March", byear="2001", aday="3", amonth="March", ayear="2001", address_2="address, 2 updated", phone_home_2="999911",
                                            notes="notes_updated"))
    app.session.logout()