from django.contrib.auth import logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render

def logout_view(request):
    logout(request)
    return redirect('ShopHome')