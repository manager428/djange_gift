from django.contrib import messages
from django.http.response import HttpResponseRedirect
from shop.models import OrderProduct


def cancelProduct(request, orid, prid):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    product = OrderProduct.objects.get(order_id=orid, user_id=current_user.id, product_id=prid)
    product.status = 'Cancelled'
    product.save()
    messages.success(request, product.product.product_name + " has been cancelled.")
    return HttpResponseRedirect(url)
