from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from .models import Item, Comment, Order, OrderElement
from django.contrib.auth.models import User
from .forms import CommentForm, AddToCartForm, OrderForm
from django.conf import settings
from .Cart import Cart

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
        'cart_items': Cart(request.session).to_list(),
        'order_form': OrderForm()
    }

    cart_sum = 0
    for item in context['cart_items']:
        cart_sum += (item[0].price * item[1])
    context['cart_sum'] = cart_sum

    return render(request, pattern, context)


def clear_cart(request):
    pattern = 'Shop/Cart.html'
    context = {
        'cart_items': []
    }

    Cart(request.session).clear()

    return render(request, pattern, context)


def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name', None)
            email = form.cleaned_data.get('email', None)
            new_order = Order(name=name, email=email, is_done=False)
            new_order.save()

            order_items = Cart(request.session).to_list()
            for i in order_items:
                item = i[0]
                amount = i[1]
                order_item = OrderElement(order=new_order, item=item, amount=amount)
                order_item.save()

    Cart(request.session).clear()
    return redirect('ShopApp:cart')