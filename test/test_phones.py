import re #импорт для работы с регулярными выражениями

def test_fields_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0] #индекс 0 - первый контакт
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.name == clear(contact_from_edit_page.name)
    assert contact_from_home_page.lastname == clear(contact_from_edit_page.lastname)
    assert contact_from_home_page.address_1 == clear(contact_from_edit_page.address_1)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)



#def test_phones_on_contact_view_page(app):
    #contact_from_view_page = app.contact.get_contact_from_view_page(0)  # индекс 0 - первый контакт
    #contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    #assert contact_from_view_page.phone_home == contact_from_edit_page.phone_home
    #assert contact_from_view_page.mobile_home == contact_from_edit_page.mobile_home
    #assert contact_from_view_page.phone_work == contact_from_edit_page.phone_work
    #assert contact_from_view_page.phone_home_2 == contact_from_edit_page.phone_home_2


def clear(s): #метод для очистки поля
    return re.sub("[ \n () -]", "", s) #первый параметр - шаблон(что заменять)/второй - на что заменять/ третий - где заменять


def clear_emails(s): #метод для очистки поля
    return re.sub(" +", " ", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                             map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                    [contact.phone_home, contact.mobile_home, contact.phone_work, contact.phone_home_2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_emails(x),
                                filter(lambda x: x is not None,
                                       [contact.email_1, contact.email_2, contact.email_3]))))

