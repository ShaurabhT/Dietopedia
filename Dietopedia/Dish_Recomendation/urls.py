from django.urls import path
from . import views


urlpatterns =[
    path('Recomendation',views.Recommend,name="Dish Recommendation"),
    path('Logout',views.Logout,name="Logout"),
    # path('index', views.index, name='index'),
	path('foodresults', views.foodresults, name='foodresults'),
   
]