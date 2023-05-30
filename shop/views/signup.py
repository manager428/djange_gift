from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponseRedirect
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from shop.models import Customer

class Signup(View):
    def get(self, request):
        current_user = request.user
        if current_user.id:
            messages.success(request, 'Already logged in!!!')
            return redirect('ShopHome')
        return render(request, 'signup.html')

    def post(self, request):
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        house = request.POST['house']
        street = request.POST['street']
        state = request.POST['state']
        city = request.POST['city']
        pin = request.POST['pin']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        uname = email
        print(uname, fname, lname, email, phone, pass1)

        values = {
            'email': email,
            'fname': fname,
            'lname': lname,
            'phone': phone,
            'house': house,
            'street': street,
            'state': state,
            'city': city,
            'pin': pin,
        }

        # Form Validations
        if User.objects.filter(email=email):
            messages.success(request, "E-mail Already Registered!!!")
            return render(request, 'signup.html', values)
        if len(fname)>10 and len(lname)>10:
            messages.success(request, "First or Last Name too long!!!")
            return render(request, 'signup.html', values)
        if not fname.isalpha() or not lname.isalpha():
            messages.warning(request,"Name must contain only letters.")
            return render(request, 'signup.html', values)
        if len(str(phone))!=10:
            messages.warning(request,"Phone number must contain 10 digits.")
            return render(request, 'signup.html', values)
        if len(pass1)<5:
            messages.warning(request, "Password too short!!! It must have atleast 5 characters.")
            return render(request, 'signup.html', values)
        if pass1!=pass2:
            messages.warning(request, "Passwords don't match!!!")
            return render(request, 'signup.html', values)

        new_user = User.objects.create_user(
            uname,
            email=email,
            password=pass1,
            first_name=fname.capitalize(),
            last_name=lname.capitalize(),
            )
        new_user.save()

        customer = Customer(
            user=new_user,
            phone=phone,
            house_no=house,
            street=street.capitalize(),
            state=state.capitalize(),
            city=city.capitalize(),
            pin=pin,
        )
        customer.save()

        user = authenticate(request, username=email, password=pass1)
        if user is not None:
            login(request, user)

        messages.success(request, "Account Created Successfully!!!")
        return redirect('ShopHome')
        