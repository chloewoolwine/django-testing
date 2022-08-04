from django.urls import path
#from .views import homePageView
from . import views

urlpatterns = [
    path('login/',views.login, name="login"),
    path('reset/',views.reset, name="reset"),
    path('register/',views.register, name="register")
]