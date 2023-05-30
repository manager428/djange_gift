from shop.models import Customer, Cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='/login')
def cart(request):
    current_user = request.user
    customer = Customer.objects.get(user_id=current_user.id)
    carts = Cart.objects.filter(user_id=current_user.id)

    total = 0
    qty = 0
    for cart in carts:
        total = total + cart.amount
        qty = qty + cart.qty
    
    discount = 10/100 * total
    if discount > 20000:
        discount = 20000

    grand_total = total - discount
    
    cart = {
        'customer':customer,
        'carts':carts,
        'qty':qty,
        'total':total,
        'discount':discount,
        'grand_total':grand_total,
    }
    
    return render(request, 'cart.html', cart)