import re #импорт для работы с регулярными выражениями

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0] #индекс 0 - первый контакт
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.phone_home == clear(contact_from_edit_page.phone_home)
    assert contact_from_home_page.mobile_home == clear(contact_from_edit_page.mobile_home)
    assert contact_from_home_page.phone_work == clear(contact_from_edit_page.phone_work)
    assert contact_from_home_page.phone_home_2 == clear(contact_from_edit_page.phone_home_2)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)  # индекс 0 - первый контакт
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.phone_home == contact_from_edit_page.phone_home
    assert contact_from_view_page.mobile_home == contact_from_edit_page.mobile_home
    assert contact_from_view_page.phone_work == contact_from_edit_page.phone_work
    assert contact_from_view_page.phone_home_2 == contact_from_edit_page.phone_home_2


def clear(s): #метод для очистки поля
    return re.sub("[ () -]", "", s) #первый параметр - шаблон(что заменять)/второй - на что заменять/ третий - где заменять
