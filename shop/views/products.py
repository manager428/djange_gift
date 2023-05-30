from django.shortcuts import render
from shop.models import Category, Customer, Product, Cart

def products(request):
    current_user = request.user
    customer = []
    try:
        customer = Customer.objects.get(user_id=current_user.id)
    except:
        pass
    categories = Category.objects.all()

    categoryid = 0
    filtered_category = []

    try:
        categoryid = request.GET['category']
    except:
        pass

    if categoryid:
        products = Product.objects.filter(category_id=categoryid)
        filtered_category = Category.objects.get(id=categoryid)
    else:
        products = Product.objects.all()
    
    n = len(products)

    current_user = request.user
    carts = Cart.objects.filter(user_id=current_user.id)
    qty = 0
    total = 0
    for cart in carts:
        total = total + cart.amount
        qty = qty + cart.qty

    params = {
        'customer':customer,
        'products': products,
        'categories': categories,
        'filtered_category': filtered_category,
        'n': n,
        'qty': qty,
        'total':total,
        'carts':carts,
        }
    
    return render(request, 'products.html', params)