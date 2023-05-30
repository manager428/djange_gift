from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from shop.models import Customer, Cart

@login_required(login_url='/login')
def updateprofile(request):
    if request.method == "GET":
        current_user = request.user
        carts = Cart.objects.filter(user_id=current_user.id)
        qty = 0
        total = 0
        for cart in carts:
            total = total + cart.amount
            qty = qty + cart.qty
        customer = Customer.objects.get(user_id=current_user.id)
        details = {
            'customer':customer,
            'qty':qty,
            'total':total,
            'carts':carts,
        }
        return render(request, 'updateprofile.html', details)

    if request.method == "POST":
        current_user = request.user
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        house = request.POST['house']
        street = request.POST['street']
        state = request.POST['state']
        city = request.POST['city']
        pin = request.POST['pin']
        profile_pic=''
        try:
            profile_pic = request.FILES['pic']
        except:
            pass
        
        # Form Validations
        if len(fname)>10 and len(lname)>10:
            messages.success(request, "First or Last Name too long!!!")
            return HttpResponseRedirect('/account/updateprofile')
        if not fname.isalpha() or not lname.isalpha():
            messages.warning(request,"Name must contain only letters.")
            return HttpResponseRedirect('/account/updateprofile')
        if len(str(phone))!=10:
            messages.warning(request,"Phone number must contain 10 digits.")
            return HttpResponseRedirect('/account/updateprofile')

        update_user = User.objects.get(id=current_user.id)
        update_user.username=email
        update_user.first_name=fname
        update_user.last_name=lname
        update_user.email=email
        update_user.save()

        update_customer = Customer.objects.get(user_id=update_user.id)
        update_customer.phone=phone
        update_customer.house_no=house
        update_customer.street=street
        update_customer.state=state
        update_customer.city=city
        update_customer.pin=pin
        if profile_pic:
            update_customer.profile_pic=profile_pic
        update_customer.save()

        messages.success(request, "Your Account has been successfully updated!!!")
        return redirect('Account')
        