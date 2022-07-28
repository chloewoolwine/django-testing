from django.urls import path
#from .views import homePageView
from . import views

urlpatterns = [
    path("", views.home, name="pages-home"),
    path('about/',views.about, name="pages-about")
]