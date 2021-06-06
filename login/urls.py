from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.loginPage, name='login'),
    # path('', views.logoutUser, name='logout'),
    path('userhome/', include('userhome.urls')),

]