from shop.models import Customer, Cart
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

@login_required(login_url='/login')
def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password has been successfully changed!!!')
            return redirect('Account')
        else:
            messages.error(request, str(form.errors))
            return HttpResponseRedirect('/account/changepassword')
    else:
        current_user = request.user
        customer = Customer.objects.get(user_id=current_user.id)
        carts = Cart.objects.filter(user_id=current_user.id)
        qty = 0
        total = 0
        for cart in carts:
            total = total + cart.amount
            qty = qty + cart.qty
        form = PasswordChangeForm(request.user)
        details = {
            'customer':customer,
            'qty':qty,
            'total':total,
            'carts':carts,
        }
        return render(request, 'changepassword.html', details)