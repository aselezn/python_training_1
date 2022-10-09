from model.contact import Contact
from random import randrange
import random

def test_del_some_contact(db, app):
    if not len(db.get_contact_list()):
        app.contact.create_contact(Contact(name="name", middlename="middlename", lastname="lastname", nickname="nickname", title="title", company="company", address_1="address, 1",
                                           phone_home="55555", mobile_home="22222", phone_work="33333", fax="44444", email_1="email1@mail.ru", email_2="email2@mail.ru", email_3="email3@mail.ru",
                                           homepage="homepage", bday= "1", bmonth="January", byear="2000", aday="2", amonth="February", ayear="2000", address_2="address, 2", phone_home_2="9999",
                                           notes="notes"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts

