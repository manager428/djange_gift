from django.shortcuts import render
from shop.models import Category, Customer, Product, Cart


def searchMatch(search, prod):
    if search.lower() in prod.description.lower() or search in prod.product_name.lower() or search in prod.category.category_name.lower():
        return True
    else:
        return False

def checkCategory(categoryid, prod):
    if prod.category_id == int(categoryid):
        return True
    else:
        return False

def search(request):
    current_user = request.user
    customer = []
    try:
        customer = Customer.objects.get(user_id=current_user)
    except:
        pass

    search = request.GET['search']
    products = []
    categoryid = 0

    try:
        categoryid = request.GET['category']
    except:
        pass

    allproducts = Product.objects.all()
    categories = Category.objects.all()

    for products in allproducts:
        if categoryid:
            products = [prod for prod in allproducts if searchMatch(search, prod) and checkCategory(categoryid, prod)]
        else:
            products = [prod for prod in allproducts if searchMatch(search, prod)]

    n = len(products)

    current_user = request.user
    carts = Cart.objects.filter(user_id=current_user.id)
    qty = 0
    total = 0
    for cart in carts:
        total = total + cart.amount
        qty = qty + cart.qty

    params = {
        'customer': customer,
        'products': products,
        'n': n,
        'search': search.lower(),
        'categories': categories,
        'qty': qty,
        'total':total,
        'carts':carts,
    }
    return render(request, 'search.html', params)
