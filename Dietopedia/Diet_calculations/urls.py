from django.urls import path
from . import views


urlpatterns =[
    path('BMR',views.BMR,name="BMR"),
    path('BDI',views.BDI,name="BDI"),
    path('History',views.History,name="History"),
    path('Logout',views.Logout,name="Logout"),
    path('Report',views.Report,name="Report"),
    
]