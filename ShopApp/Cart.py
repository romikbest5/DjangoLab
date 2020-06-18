from .models import Item
from django.conf import settings

class Cart:
    def __init__(self, session):
        self.session = session
        cart = self.session.get(settings.CART_SESSION_IDENTIFIER)
        if not cart:
            cart = self.session[settings.CART_SESSION_IDENTIFIER] = []
            self.session[settings.CART_SESSION_SIZE_IDENTIFIER] = 0
        self.cart = cart

    def add(self, item_id, quantity):
        id = str(item_id)
        updated = False
        for elem in self.cart:
            if elem['id'] == id:
                elem['quantity'] += quantity
                updated = True
        if not updated:
            self.cart.append({'id': id, 'quantity': quantity})
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_IDENTIFIER] = self.cart
        self.session[settings.CART_SESSION_SIZE_IDENTIFIER] = self.count()
        self.session.modified = True

    def clear(self):
        self.session[settings.CART_SESSION_IDENTIFIER] = []
        self.session[settings.CART_SESSION_SIZE_IDENTIFIER] = 0
        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def count(self):
        counter = 0
        for elem in self.cart:
            counter += elem['quantity']
        return counter

    def to_list(self):
        items_id = []
        res_list = []
        for elem in self.cart:
            items_id.append(int(elem['id']))
            res_list.append([items_id[-1], elem['quantity']])
        res_list.sort()
        items = Item.objects.filter(id__in=items_id).order_by('id')
        for i in range(len(res_list)):
            res_list[i][0] = items[i]
        return res_list