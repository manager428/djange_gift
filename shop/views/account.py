from shop.models import Category, Customer, Order, OrderProduct, Cart, Wishlist
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User

@login_required(login_url='/login')
def account(request):
    orderprs=[]
    currentuser = request.user

    carts = Cart.objects.filter(user_id=currentuser.id)
    qty = 0
    total = 0
    for cart in carts:
        total = total + cart.amount
        qty = qty + cart.qty
    
    categories = Category.objects.all()
    customer = Customer.objects.get(user_id=currentuser.id)
    wishlists = Wishlist.objects.filter(user_id=currentuser.id)

    orders = Order.objects.filter(user_id=currentuser.id).order_by("-placed_at")
    for order in orders:
        pr = OrderProduct.objects.filter(order_id=order.id)
        orderprs.append(pr)
    
    details = {
        'customer':customer,
        'orders':orders,
        'orderprs':orderprs,
        'qty':qty,
        'total':total,
        'carts':carts,
        'categories':categories,
        'wishlists':wishlists
        }

    return render(request, 'account.html', details)