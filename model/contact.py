from sys import maxsize


class Contact:

    def __init__(self, name=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address_1=None, phone_home=None, mobile_home=None, phone_work=None, email_1=None, email_2=None,
                 email_3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, address_2=None, phone_home_2=None, notes=None, fax=None, id=None):
        self.name = name
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address_1 = address_1
        self.phone_home = phone_home
        self.mobile_home = mobile_home
        self.phone_work = phone_work
        self.fax = fax
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address_2 = address_2
        self.phone_home_2 = phone_home_2
        self.notes = notes
        self.id = id


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize








