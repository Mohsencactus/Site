from . import views
from django.urls import path,include
from .views import accounts,loginpage,registerpage,logoutpage

urlpatterns = [
    path('', accounts),
    path('login/', loginpage),
    path('register/', registerpage),
    path('logout/', logoutpage)
]