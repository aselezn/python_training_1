# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.fill_contact_form(Contact (name="name", middlename="middlename", lastname="lastname", nickname="nickname", title="title", company="company", address_1="address, 1",
                                            phone_home="55555", mobile_home="22222", phone_work="33333", fax="44444", email_1="email1@mail.ru", email_2="email2@mail.ru", email_3="email3@mail.ru",
                                            homepage="homepage", bday= "1", bmonth="January", byear="2000", aday="2", amonth="February", ayear="2000", address_2="address, 2", phone_home_2="9999",
                                            notes="notes"))
    app.session.logout()



