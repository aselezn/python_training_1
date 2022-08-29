from model.contact import Contact

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(name="name", middlename="middlename", lastname="lastname", nickname="nickname", title="title", company="company", address_1="address, 1",
                                        phone_home="55555", mobile_home="22222", phone_work="33333", fax="44444", email_1="email1@mail.ru", email_2="email2@mail.ru", email_3="email3@mail.ru",
                                        homepage="homepage", bday= "1", bmonth="January", byear="2000", aday="2", amonth="February", ayear="2000", address_2="address, 2", phone_home_2="9999",
                                        notes="notes"))
    app.contact.modify_first_contact(Contact (name="name_updated", middlename="middlename_updated", lastname="lastname_updated", nickname="nickname_updated", title="title_updated", company="company_updated", address_1="address, 1 updated",
                                              phone_home="5555511", mobile_home="2222211", phone_work="3333311", fax="4444411", email_1="email_1_updated@mail.ru", email_2="email_2_updated@mail.ru", email_3="email_3_updated@mail.ru",
                                              homepage="homepage_updated", bday= "2", bmonth="March", byear="2001", aday="3", amonth="March", ayear="2001", address_2="address, 2 updated", phone_home_2="999911",
                                              notes="notes_updated"))
