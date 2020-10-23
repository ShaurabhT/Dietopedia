from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import auth
# Create your views here.
@login_required(login_url='../log/signin')
@user_passes_test(lambda u: u.groups.filter(name='Customers').exists(),login_url='../Dietitian/')
def Profile(request):
    return render(request,"Profile.html")
def Logout(request):
    auth.logout(request)
    return redirect("/")