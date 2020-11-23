from django.shortcuts import render,redirect
from . import test_api2
from django.contrib import auth
from Login.models import Customers
from Diet_calculations.models import Calculations
from Dish_Recomendation import test_api
from Dish_Recomendation.health_input import *
from Dish_Recomendation.health_api import *
from Login.models import Customers

# Create your views here.

def Recommend(request):
    user=request.user
    calories_1 = Calculations.objects.filter(user=user,fieldname="BMR").values().latest('date')
    calories=calories_1["BMR"]
    # name=test_api.create_url()
    return render(request,"Dish_rec.html")

def Logout(request):
    auth.logout(request)
    return redirect("/")

def foodresults(request):
    user=request.user
    if Calculations.objects.filter(user=user,fieldname="BMR").values().exists():
        calories_1 =Calculations.objects.filter(user=user,fieldname="BMR").values().latest('date')
        calories=round(calories_1["BMR"])
        meals = generate_meals(int(calories))
        exerciselvl=calories_1["Exerciselvl"]  #done
        context = {'totalCalories': calories, 'breakfast': meals[0], 'lunch': meals[1], 'dinner': meals[2],'exerciselvl':exerciselvl}
        context['mealCalories'] = context['breakfast']['calories'] + context['lunch']['calories'] + context['dinner']['calories']
        return render(request, 'foodresults.html', context)
    else:
        response = redirect('../calculator/BMR')
        return response
    