from django.urls import path
from apps.users.views import Login,Logout, Home
urlpatterns = [
    path('home/', Home.as_view(), name='Home'),
    path('login/', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name= 'logut')
]
