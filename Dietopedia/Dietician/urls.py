
from django.urls import path
from Dietician import views
from django.conf.urls.static import static
from django.conf import settings
from Dietician.views import Inbox, UserSearch, Directs, NewConversation, SendDirect


urlpatterns =[
    path('',views.Profile,name="Profile"),
    path('Logout',views.Logout,name="Logout"),
    path('inbox', Inbox, name='inbox'),
   	path('directs/<username>', Directs, name='directs'),
   	path('new/', UserSearch, name='usersearch'),
   	path('new/<username>', NewConversation, name='newconversation'),
   	path('send/', SendDirect, name='send_direct'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
