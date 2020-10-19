from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from .models import CalculationsBMI,CalculationsBDI
from django.contrib.auth.models import User
from Login.models import Customers



# Create your views here.
@login_required(login_url='../log/signin')
def BMR(request):
     if  request.method== 'POST':
        height =request.POST['height']
        weight=request.POST['weight']
        user=request.user
        age =request.POST['age']
        Gender=request.POST['gender']
        exer =request.POST['exercise']
        if height =='' :
            print(age)
            if weight =='':
                if age =='':
                 return render(request,"Diet_calculations/BMR.html")
        else:
            if Gender == '1' :
                bmr = 66 + ( 6.23 * float(weight)) + ( 12.7 *float(height)  ) - ( 6.8 * float(age)  )
                if (exer == '1'):
                    bdiwithexercise= bmr*1.2
                            
                elif (exer == '2'):
                    bdiwithexercise= bmr*1.375
                            
                elif (exer == '3'):
                    bdiwithexercise= bmr*1.55
                            
                elif (exer == '4'):
                    bdiwithexercise= bmr*1.725
                            
                elif (exer == '5'):
                    bdiwithexercise= bmr*1.9
                
                user=request.user
                addbdio= CalculationsBMI(user=user,BMR=bdiwithexercise)
                addbdio.save()
                return render(request,"Diet_calculations/BMR.html")
            else:
                bmr =655 + ( 4.35 * float(weight)) + ( 4.7 * float(height) ) - ( 4.7 * float(age))
                if (exer== '1'):
                    bdiwithexercise= bmr*1.2
                            
                elif (exer== '2'):
                    bdiwithexercise= bmr*1.375
                            
                elif (exer== '3'):
                    bdiwithexercise= bmr*1.55
                            
                elif (exer== '4'):
                    bdiwithexercise= bmr*1.725
                            
                elif (exer== '5'):
                    bdiwithexercise= bmr*1.9
                
                user=request.user 
                test=CalculationsBMI.objects.filter(user=user).last()
                user=request.user
                addbdio= CalculationsBMI(user=user,BMR=bdiwithexercise)
                addbdio.save() 
                return render(request,"Diet_calculations/BMR.html",{"test":test})
           

             
     else:
        user=request.user 
        test=CalculationsBMI.objects.filter(user=user).last()
        return render(request,"Diet_calculations/BMR.html",{"test":test})

         
    
@login_required(login_url='../log/signin')    
def BDI(request):
    if  request.method== 'POST':
        heightfet =request.POST['heightft']
        heightin =request.POST['heightinc']
        weight=request.POST['weight']
        waist=request.POST['waist']
        butt=request.POST['butt']

        if (int(heightin)>11):
            remainderinc= 12 % int(heightin)
            heightinc2=remainderinc
            heightft2=int(heightfet)+((int(heightin)-int(remainderinc))/12) 
        else:
            HeightFeetConvert = int(heightfet) * 12
            remainderinc=int(heightin)%12
            height=HeightFeetConvert+remainderinc

           
        if 2<int(height)<213:   
            if 15<int(weight)<200:
                if 12<int(waist)<4000 :
                    if 12<int(butt)<4000:
                        BDI = (int(weight) * 703 * (int(waist) + int(butt)) )/ (int(height)*int(height)*int(height))
                        user=request.user 
                        test=CalculationsBDI.objects.filter(user=user).last()
                        user=request.user
                        addbdi= CalculationsBDI(user=user,BDI=BDI)
                        addbdi.save() 
                        if int(BDI)<5:
                            messages.info(request,"Probably Dead and dried")
                            return render(request,"Diet_calculations/BDI.html",{"bdi":addbdi})
                        
                        elif 10>int(BDI)>5:
                            messages.info(request,"Near Death")
                            return render(request,"Diet_calculations/BDI.html",{"bdi":addbdi})
                        
                        elif 10>int(BDI)>11.5:
                            messages.info(request,"Unmoving skeleton")
                            return render(request,"Diet_calculations/BDI.html",{"bdi":addbdi})
                        
                        elif 13.5>int(BDI)>11.5:
                            messages.info(request,"Crawling bones")
                            return render(request,"Diet_calculations/BDI.html",{"bdi":addbdi})
                        
                        elif 16>int(BDI)>13.5:
                            messages.info(request,"Walking sticks")
                            return render(request,"Diet_calculations/BDI.html",{"bdi":addbdi})
                        
                        elif 18.5>int(BDI)>16:
                            messages.info(request,"Running fox")
                            return render(request,"Diet_calculations/BDI.html",{"bdi":addbdi})
                        
                        elif 21.5>int(BDI)>18.5:
                            messages.info(request,"Jogging coyote")
                            return render(request,"Diet_calculations/BDI.html",{"bdi":addbdi})
                        
                        elif 25.2>int(BDI)>21.5:
                            messages.info(request,"Gamboling pony")
                            return render(request,"Diet_calculations/BDI.html",{"bdi":addbdi})
                        
                        elif 25.2>int(BDI):
                            messages.info(request,"Beyond human")
                            return render(request,"Diet_calculations/BDI.html",{"bdi":addbdi})
                        
        else:
            messages.info(request,"Incorrect value")
            return render(request,"Diet_calculations/BDI.html")
           
    else:
        user=request.user 
        test=CalculationsBDI.objects.filter(user=user).last()
        messages.info(request,"Enter value")
        return render(request,"Diet_calculations/BDI.html",{"bdi":test})

    
    

    


@login_required(login_url='../log/signin')
def Profile(request):


    
    return render(request,"Diet_calculations/Profile.html",{})
@login_required(login_url='../log/signin')


def History(request):
    user=request.user
    all_bmr=CalculationsBMI.objects.filter(user=user)
    all_bdi=CalculationsBDI.objects.filter(user=user)
    return render(request,"Diet_calculations/History.html",{"bmi":all_bmr,"bdi":all_bdi})


def Logout(request):
    auth.logout(request)
    return redirect("/")