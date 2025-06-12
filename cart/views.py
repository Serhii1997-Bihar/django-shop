from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from cart.cart import Cart
from cart.forms import *
from django.contrib import messages

@require_POST
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(ProductsModel, id=id)

    if request.method == 'POST':
        sizes = product.size.all()
        form = CartAddProductForm(sizes=sizes, data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'], size_id=cd['size'])
            messages.add_message(request, messages.SUCCESS, 'Додано в корзину')
            return redirect('detailpage', product.id)
    else:
        form = CartAddProductForm(sizes=product.size.all())

    return redirect('mainpage')

def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(ProductsModel, id=id)
    cart.remove(product)
    return redirect('cart')

def cart_detail(request):
    cart = Cart(request)
    context = {'cart': cart}
    return render(request, 'cart_templates/cart_products.html', context)

def order(request):
    cart = Cart(request)
    form = OrderForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        address = form.cleaned_data['address']
        phone = form.cleaned_data['phone']
        mail = form.cleaned_data['mail']
        comment = form.cleaned_data['comment']
        order = ClientData.objects.create(name=name, address=address, phone=phone, mail=mail, comment=comment)
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'],
                                     size=item['size'])

        order.total_price = cart.get_total_price()
        order.save()
        cart.clear()
        return redirect('cart')
    return render(request, 'cart_templates/order.html', {'cart': cart, 'form': form})

