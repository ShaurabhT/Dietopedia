from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth,Group
from django.contrib import messages
from .models import Customers

# Create your views here.

def SignUp(request):

    if  request.method== 'POST':
        username= request.POST["uname"]
        First_Name=request.POST["fname"]
        email= request.POST["email"]
        Password=request.POST["password"]
        CPassword=request.POST["cpassword"]
        Gender=request.POST["gender"]
        Age=request.POST["age"]
        dietitian=request.POST['dietitian']
      
        if Password==CPassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username Exists")
                return(redirect('/log/signup/'))
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already Exists")
                return(redirect('/log/signup/'))
            else:
                if dietitian =="Yes":
                    user=User.objects.create_user(username=username,first_name=First_Name,password=Password,email=email)
                    if  User.objects.filter(groups__name="Dietitians").exists():
                        user.groups.add(Group.objects.get(name='Dietitians'))
                        user.save()
                        newextended= Customers(Gender=Gender,Age=Age,user=user)
                        newextended.save()
                        return(redirect('/log/signin/'))
                    else:
                        Group.objects.get_or_create(name="Dietitians")
                        user.groups.add(Group.objects.get(name='Dietitians'))
                        user.save()
                        newextended= Customers(Gender=Gender,Age=Age,user=user)
                        newextended.save()
                        return(redirect('/log/signin/'))
                    
                   
                    
                elif dietitian =="No":
                    user=User.objects.create_user(username=username,first_name=First_Name,password=Password,email=email)
                    if  User.objects.filter(groups__name="Customers").exists():
                        user.groups.add(Group.objects.get(name='Customers'))
                        user.save()   
                        newextended= Customers(Gender=Gender,Age=Age,user=user)
                        newextended.save()
                        return(redirect('/log/signin/'))
                    else:
                        Group.objects.get_or_create(name="Customers")
                        user.groups.add(Group.objects.get(name='Customers'))
                        user.save()
                        newextended= Customers(Gender=Gender,Age=Age,user=user)
                        newextended.save()
                        return(redirect('/log/signin/'))
                    
        else:
            messages.info(request,"Password not matching")
            return(redirect('/log/signup/'))
    else:
       return render(request,"signup.html",{})
    

def SignIn(request):
        if request.method == "POST":
            username=request.POST['Username']
            password=request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                if user.groups.filter(name = 'Customers').exists():
                    return (redirect('/profile/'))
                else:
                    return  (redirect('/Dietitian/'))
            else:
                messages.info(request,"Invalid Credentials")
                return (redirect('/log/signin'))
        else:
         return render(request,"signin.html",{})    

def Logout(request):
    auth.logout(request)
    return redirect("/")