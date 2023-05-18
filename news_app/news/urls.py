from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('search/',views.search,name='search'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('about/',views.about,name='about'),
    path('newsletter/',views.newsletter,name='newsletter'),
    path('colors/',views.color,name='color'),
    path('illusions/',views.illusion,name='illusion'),
    path('events',views.event,name='event'),
    path('tourist-places',views.place,name='place'),
]
