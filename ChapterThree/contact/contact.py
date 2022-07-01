"""联系人类 multiple inheritance"""


class ContactList(list):
    """联系人列表, 处理联系人问题"""
    def search(self, name):
        """根据 name 搜索联系人列表并返回结果"""
        result = list()
        for i, con in enumerate(Contact.all_contacts):
            if con.name == name:
                result.append(con)
        return result


class Contact:
    all_contacts = ContactList()

    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print(f'This is a real system we would send {order} order to {self.name}')


class AddressHolder:
    """a kind of person who is an address holder"""
    def __init__(self, street='', **kwargs):
        # super().__init__(**kwargs)
        self.street = street


class Friend(Contact, AddressHolder):
    """one class for friends to save their phone number"""
    def __init__(self, phone='', **kwargs):
        kwargs.update(dict(phone=phone))
        super().__init__(**kwargs)
        AddressHolder.__init__(self, **kwargs)
        self.phone = phone


if __name__ == '__main__':
    f = Friend(phone='222', street='Yingze Street', name='Rock', email='rock@gmail.com')
    print(f.name, f.phone, f.street)

