# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10  # в переменной будут буквы + символы + пунктуация + 10 раз повторяем пробел
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])  # генерируется случайная длина строки не превышающая максимальную

def random_number(prefix):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(10)])


testdata = [Contact(name="", middlename="", lastname="", nickname="", title="", company="", address_1="",
                      phone_home="", mobile_home="", phone_work="", fax="",
                      email_1="", email_2="", email_3="",
                      homepage="",
                      bday= "", bmonth="", byear="", aday="", amonth="", ayear="",
                      address_2="", phone_home_2="",
                      notes="")] + [
             Contact(name=random_string("name",10), middlename=random_string("middlename",10), lastname=random_string("lastname",10), nickname=random_string("nickname",10), company=random_string("company",10), title=random_string("title",10),
             address_1=random_string("address_1",20),
             phone_home=random_number("+79"), mobile_home=random_number("+79"), phone_work=random_number("+79"), fax=random_number("8"),
             email_1="email1@mail.ru", email_2="email2@mail.ru", email_3="email3@mail.ru",
             homepage=random_string("homepage", 10),
             bday="1", bmonth="January", byear="2000", aday="2", amonth="February", ayear="2000",
             address_2=random_string("address_2", 20), phone_home_2=random_number("+79"),
             notes=random_string("notes", 10))
             for i in range(5)] #5 раз создаем контакт с рандомными данными



@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)








