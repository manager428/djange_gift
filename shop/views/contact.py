from shop.models import Category, Customer, Cart
from django.shortcuts import render

def contact(request):
    current_user = request.user

    customer = []
    try:
        customer = Customer.objects.get(user_id=current_user.id)
    except:
        pass
    
    carts = Cart.objects.filter(user_id=current_user.id)
    categories = Category.objects.all()
    
    qty = 0
    total = 0
    for cart in carts:
        total = total + cart.amount
        qty = qty + cart.qty
    
    details = {
        'customer':customer,
        'qty':qty,
        'total':total,
        'carts':carts,
        'categories':categories
    }
    return render(request, 'contactus.html', details)