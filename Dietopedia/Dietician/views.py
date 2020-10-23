from django.shortcuts import render,redirect
from django.contrib.auth.decorators import  user_passes_test,login_required
from django.contrib import auth
# Create your views here.



@login_required
@user_passes_test(lambda u: u.groups.filter(name='Dietitians').exists(),login_url='../profile')
def Profile(request):
    return render(request,"dietitian.html")


def Logout(request):
    auth.logout(request)
    return redirect("/")

def requestmessage(request):
    return render(request,"request_message.html")
    