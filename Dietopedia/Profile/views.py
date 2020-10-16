from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='../log/signinc')
def Profile(request):
    return render(request,"Profile.html")
