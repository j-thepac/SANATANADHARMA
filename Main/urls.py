from django.urls import path,include
from . import views
from Main import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    # path('', views.logoutUser, name='logout'),
    path('userhome/', views.user_home, name='user_home'),
    path('', views.index, name='index'),
]