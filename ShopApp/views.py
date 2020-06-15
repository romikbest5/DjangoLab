from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import Item, Comment
from django.contrib.auth.models import User
from .forms import CommentForm, AddToCartForm
from django.conf import settings

def catalog(request):
    pattern = 'Shop/Catalog.html'
    context = {
        'items': Item.objects.all()
    }
    return render(request, pattern, context)


def detail(request, item_id):
    pattern = 'Shop/Detail.html'
    context = {
        'item': Item.objects.get(id=item_id),
        'comments': Comment.objects.filter(item=item_id),
        'comment_form': CommentForm(),
        'add_form': AddToCartForm()
    }

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            text = form.cleaned_data.get('text', None)
            mark = int(form.cleaned_data.get('mark', None))
            selected_item = Item.objects.get(id=item_id)
            new_comment = Comment(item=selected_item, user=request.user, text=text, mark=mark)
            new_comment.save()
            return redirect('ShopApp:detail', item_id)

    return render(request, pattern, context)

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




def add_item(request, item_id):
    pattern = 'Shop/Detail.html'
    context = {
        'item': Item.objects.get(id=item_id),
        'comments': Comment.objects.filter(item=item_id),
        'comment_form': CommentForm(),
        'add_form': AddToCartForm(),
    }
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data.get('quantity', None)
            user_cart = Cart(request.session)
            user_cart.add(item_id, quantity)

    return render(request, pattern, context)


def cart(request):
    pattern = 'Shop/Cart.html'
    context = {
        'cart_items': Cart(request.session).to_list()
    }

    return render(request, pattern, context)


def clear_cart(request):
    pattern = 'Shop/Cart.html'
    context = {
        'cart_items': []
    }

    Cart(request.session).clear()

    return render(request, pattern, context)