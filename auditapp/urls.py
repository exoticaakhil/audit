from django.urls import path
from. import views

urlpatterns = [
    path('',views.index,name='index'),
    path('features',views.features,name='features'),
    path('about',views.about,name='about'),
    path('contactus',views.contactus,name='contactus'),
    path('demo',views.demo,name='demo'),
    path('price',views.price,name='price'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
]
