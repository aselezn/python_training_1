# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="name", middlename="middlename", lastname="lastname", nickname="nickname", title="title", company="company", address_1="address, 1",
                                        phone_home="55555", mobile_home="22222", phone_work="33333", fax="44444", email_1="email1@mail.ru", email_2="email2@mail.ru", email_3="email3@mail.ru",
                                        homepage="homepage", bday= "1", bmonth="January", byear="2000", aday="2", amonth="February", ayear="2000", address_2="address, 2", phone_home_2="9999",
                                        notes="notes")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    #assert sorted(new_contacts,  key=lambda contact: contact.id_or_max())






