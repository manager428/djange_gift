from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from shop.models import Cart

@login_required(login_url='/login')
def buynow(request, prid):
    current_user = request.user
    Cart.objects.filter(user_id=current_user.id).delete()
    data = Cart()
    data.user_id = current_user.id
    data.product_id = prid
    data.qty = 1
    data.save()
    return HttpResponseRedirect('/cart')