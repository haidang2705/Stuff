from . import views
from django.urls import path
# three step to create web page
# create actual template file
# create actual HTML page
# create a URL
urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.login_user, name = 'login'),   
    path('logout/', views.logout_user, name = 'logout'),
]
