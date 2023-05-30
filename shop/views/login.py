from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from shop.models import Loginhistory, Customer
from datetime import datetime

class Login(View):
    def get(self, request):
        current_user = request.user
        if current_user.id:
            
            messages.success(request, 'Already logged in!!!')
            return redirect('ShopHome')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            current_user = request.user
            logined_date = datetime.today().strftime('%Y-%m-%d')
            
            exist_user = Loginhistory.objects.filter(user_id=request.user.pk, updated_at=logined_date)
            if exist_user.exists():
                print("this user is exited.!!!!")
            else:
                history = Loginhistory(user_id=current_user.id, logindata='1', loginyeardata='1', updated_at=logined_date)
                history.save()
            return redirect('ShopHome')
            
        else:
            messages.warning(request, "E-mail or Password Incorrect!!!")
            return render(request, 'login.html', {'email':email})
    